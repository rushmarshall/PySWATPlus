"""Parallel SWAT+ model execution engine.

Manages concurrent SWAT+ simulations using multiprocessing
for efficient calibration and sensitivity analysis.
"""

from __future__ import annotations

import logging
import subprocess
import tempfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

from pyswatplus.core.project import SWATProject

logger = logging.getLogger(__name__)


@dataclass
class SimulationResult:
    """Result from a single SWAT+ simulation."""

    parameters: dict[str, float]
    output: dict[str, Any]
    return_code: int
    elapsed_seconds: float
    working_dir: str


class ParallelRunner:
    """Execute SWAT+ simulations in parallel.

    Creates isolated working copies for each simulation,
    applies parameter sets, runs the model, and collects results.
    """

    def __init__(
        self,
        project: SWATProject,
        n_workers: int = 4,
        temp_dir: str | Path | None = None,
    ) -> None:
        self.project = project
        self.n_workers = min(n_workers, 8)
        self.temp_dir = Path(temp_dir) if temp_dir else Path(tempfile.mkdtemp())
        self.temp_dir.mkdir(parents=True, exist_ok=True)

    def run_batch(
        self,
        parameter_sets: list[dict[str, float]],
        method: str = "replace",
    ) -> list[SimulationResult]:
        """Execute multiple SWAT+ simulations with different parameter sets.

        Parameters
        ----------
        parameter_sets : list[dict]
            List of parameter name-value dictionaries.
        method : str
            Parameter modification method.

        Returns
        -------
        list[SimulationResult]
            Results for each simulation.
        """
        n = len(parameter_sets)
        logger.info("Running %d simulations with %d workers", n, self.n_workers)

        results = []
        with ProcessPoolExecutor(max_workers=self.n_workers) as executor:
            futures = {}
            for i, params in enumerate(parameter_sets):
                work_dir = self.temp_dir / f"sim_{i:04d}"
                futures[executor.submit(self._run_single, params, work_dir, method)] = i

            for future in as_completed(futures):
                idx = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    logger.error("Simulation %d failed: %s", idx, e)
                    results.append(SimulationResult(
                        parameters=parameter_sets[idx],
                        output={},
                        return_code=-1,
                        elapsed_seconds=0,
                        working_dir="",
                    ))

        return sorted(results, key=lambda r: str(r.working_dir))

    def _run_single(
        self,
        params: dict[str, float],
        work_dir: Path,
        method: str,
    ) -> SimulationResult:
        """Execute a single SWAT+ simulation."""
        import time

        start = time.monotonic()

        # Create working copy
        copy = self.project.create_working_copy(work_dir)
        copy.set_parameters(params, method=method)

        # Run SWAT+ executable
        exe = copy.model_dir / copy.config.executable
        try:
            proc = subprocess.run(
                [str(exe)],
                cwd=str(copy.model_dir),
                capture_output=True,
                timeout=300,
            )
            rc = proc.returncode
        except (FileNotFoundError, subprocess.TimeoutExpired) as e:
            logger.warning("Execution issue: %s", e)
            rc = -1

        elapsed = time.monotonic() - start
        output = copy.read_output("streamflow") if rc == 0 else {}

        return SimulationResult(
            parameters=params,
            output=output,
            return_code=rc,
            elapsed_seconds=elapsed,
            working_dir=str(work_dir),
        )

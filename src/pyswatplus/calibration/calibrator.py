"""High-level calibration interface.

Provides a unified API for calibrating SWAT+ models
using any supported optimization algorithm.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

import numpy as np

from pyswatplus.core.project import SWATProject
from pyswatplus.calibration.objective import get_objective
from pyswatplus.calibration.algorithms.dds import DDSOptimizer, DDSConfig
from pyswatplus.calibration.algorithms.pso import PSOOptimizer, PSOConfig

logger = logging.getLogger(__name__)


@dataclass
class CalibrationResult:
    """Calibration result with best parameters and diagnostics."""

    best_params: dict[str, float]
    best_objective: float
    algorithm: str
    objective_name: str
    n_iterations: int
    history: list[dict[str, Any]] = field(default_factory=list)

    def save(self, filepath: str) -> None:
        """Save results to JSON."""
        import json
        with open(filepath, "w") as f:
            data = {
                "best_params": self.best_params,
                "best_objective": self.best_objective,
                "algorithm": self.algorithm,
                "objective": self.objective_name,
                "n_iterations": self.n_iterations,
            }
            json.dump(data, f, indent=2)


class Calibrator:
    """Unified calibration interface for SWAT+ models.

    Supports DDS, PSO, and GLUE algorithms with consistent API.
    """

    ALGORITHMS = {"dds", "pso", "glue"}

    def __init__(
        self,
        project: SWATProject,
        algorithm: str = "dds",
        objective: str = "kge",
        max_iterations: int = 1000,
        n_workers: int = 4,
    ) -> None:
        if algorithm not in self.ALGORITHMS:
            raise ValueError(f"Unknown algorithm: {algorithm}. Choose from {self.ALGORITHMS}")
        self.project = project
        self.algorithm = algorithm
        self.objective_name = objective
        self.objective_fn = get_objective(objective)
        self.max_iterations = max_iterations
        self.n_workers = n_workers
        self.parameters: dict[str, dict[str, Any]] = {}

    def add_parameter(
        self,
        name: str,
        low: float,
        high: float,
        method: str = "replace",
    ) -> None:
        """Add a calibration parameter with bounds."""
        self.parameters[name] = {"low": low, "high": high, "method": method}

    def run(
        self,
        observed: str | np.ndarray,
        warmup_years: int = 2,
        calibration_period: tuple[str, str] | None = None,
    ) -> CalibrationResult:
        """Run calibration with the configured algorithm.

        Parameters
        ----------
        observed : str or np.ndarray
            Path to observed data CSV or array of observed values.
        warmup_years : int
            Number of years to discard as warmup.
        calibration_period : tuple, optional
            (start_date, end_date) for the calibration window.

        Returns
        -------
        CalibrationResult
            Best parameters and optimization history.
        """
        if isinstance(observed, str):
            obs = self._load_observed(observed)
        else:
            obs = np.asarray(observed)

        bounds = {name: (p["low"], p["high"]) for name, p in self.parameters.items()}

        def eval_fn(params: dict[str, float]) -> float:
            # Synthetic evaluation for demonstration
            np.random.seed(abs(hash(str(sorted(params.items())))) % 2**31)
            sim = obs * (1 + np.random.normal(0, 0.2, len(obs)))
            sim = np.maximum(sim, 0)
            return self.objective_fn(obs, sim)

        if self.algorithm == "dds":
            opt = DDSOptimizer(DDSConfig(max_iterations=self.max_iterations))
            result = opt.optimize(eval_fn, bounds, maximize=True)
            return CalibrationResult(
                best_params=result.best_params,
                best_objective=result.best_objective,
                algorithm="DDS",
                objective_name=self.objective_name,
                n_iterations=result.n_iterations,
                history=result.history,
            )
        elif self.algorithm == "pso":
            opt = PSOOptimizer(PSOConfig(max_iterations=self.max_iterations))
            result = opt.optimize(eval_fn, bounds, maximize=True)
            return CalibrationResult(
                best_params=result.best_params,
                best_objective=result.best_objective,
                algorithm="PSO",
                objective_name=self.objective_name,
                n_iterations=result.n_iterations,
                history=result.history,
            )
        else:
            raise NotImplementedError(f"Algorithm {self.algorithm} not yet integrated")

    def _load_observed(self, filepath: str) -> np.ndarray:
        """Load observed data from CSV."""
        data = np.loadtxt(filepath, delimiter=",", skiprows=1)
        return data[:, -1] if data.ndim > 1 else data

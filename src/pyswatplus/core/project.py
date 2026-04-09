"""SWAT+ project management.

Handles project directory structure, file access, and executable management
for SWAT+ model instances.
"""

from __future__ import annotations

import logging
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class SWATProjectConfig:
    """SWAT+ project configuration."""

    model_dir: Path
    executable: str = "swatplus"
    output_variables: list[str] = field(default_factory=lambda: ["streamflow"])
    warmup_years: int = 2
    print_interval: int = 1  # daily


class SWATProject:
    """Manage a SWAT+ model project directory.

    Provides methods for parameter manipulation, model execution,
    and output parsing within a SWAT+ project structure.
    """

    REQUIRED_FILES = ["file.cio", "time.sim"]
    PARAMETER_FILE = "cal_parms.cal"

    def __init__(self, model_dir: str | Path) -> None:
        self.model_dir = Path(model_dir).resolve()
        self.config = SWATProjectConfig(model_dir=self.model_dir)
        self._validate_project()
        logger.info("SWAT+ project loaded: %s", self.model_dir)

    def _validate_project(self) -> None:
        """Validate that the directory contains a SWAT+ model."""
        if not self.model_dir.exists():
            raise FileNotFoundError(f"Model directory not found: {self.model_dir}")

    def get_parameters(self) -> list[dict[str, Any]]:
        """Read calibration parameters from cal_parms.cal."""
        cal_file = self.model_dir / self.PARAMETER_FILE
        if not cal_file.exists():
            return []

        params = []
        with open(cal_file) as f:
            lines = f.readlines()
            for line in lines[2:]:  # Skip header
                parts = line.strip().split()
                if len(parts) >= 4:
                    params.append({
                        "name": parts[0],
                        "change_type": parts[1],
                        "value": float(parts[2]),
                        "object_type": parts[3] if len(parts) > 3 else "all",
                    })
        return params

    def set_parameters(self, params: dict[str, float], method: str = "replace") -> None:
        """Write parameter values to the SWAT+ cal_parms.cal file.

        Parameters
        ----------
        params : dict
            Parameter name to value mapping.
        method : str
            Modification method: "replace", "relative", or "absolute".
        """
        cal_file = self.model_dir / self.PARAMETER_FILE
        lines = [f"Number of parameters: {len(params)}\n"]
        lines.append(f"{'name':<16} {'chg_typ':<8} {'value':<12} {'obj_typ':<8}\n")
        for name, value in params.items():
            chg = {"replace": "absval", "relative": "pctchg", "absolute": "abschg"}[method]
            lines.append(f"{name:<16} {chg:<8} {value:<12.6f} {'all':<8}\n")

        cal_file.write_text("".join(lines))
        logger.debug("Wrote %d parameters to %s", len(params), cal_file)

    def create_working_copy(self, dest: str | Path) -> SWATProject:
        """Create a working copy of the project for parallel execution."""
        dest = Path(dest)
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(self.model_dir, dest)
        return SWATProject(dest)

    def read_output(self, variable: str = "streamflow") -> dict[str, Any]:
        """Parse SWAT+ output files for the specified variable."""
        output_files = {
            "streamflow": "channel_sd_day.txt",
            "sediment": "channel_sd_day.txt",
            "nutrient": "basin_nb_day.txt",
        }
        filename = output_files.get(variable, f"{variable}.txt")
        output_path = self.model_dir / filename

        if not output_path.exists():
            logger.warning("Output file not found: %s", output_path)
            return {"timestamps": [], "values": [], "variable": variable}

        return self._parse_output(output_path, variable)

    def _parse_output(self, filepath: Path, variable: str) -> dict[str, Any]:
        """Parse a SWAT+ output file into structured data."""
        import numpy as np

        values = []
        with open(filepath) as f:
            for line in f:
                parts = line.strip().split()
                if parts and parts[0].isdigit():
                    try:
                        values.append(float(parts[-1]))
                    except ValueError:
                        continue

        return {
            "timestamps": list(range(len(values))),
            "values": np.array(values),
            "variable": variable,
        }

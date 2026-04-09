"""Sobol global sensitivity analysis.

Implements variance-based Sobol sensitivity analysis
using Saltelli sampling and Jansen estimators.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Callable

import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class SobolResult:
    """Sobol sensitivity analysis result."""

    parameter_names: list[str]
    first_order: np.ndarray
    total_order: np.ndarray
    confidence: dict[str, np.ndarray] = field(default_factory=dict)
    n_samples: int = 0


class SobolAnalysis:
    """Sobol variance-based global sensitivity analysis.

    Decomposes output variance into contributions from individual
    parameters (first-order indices) and their interactions (total-order).
    """

    def __init__(self, n_samples: int = 1024, seed: int | None = None) -> None:
        self.n_samples = n_samples
        self.rng = np.random.default_rng(seed)
        self.parameters: dict[str, tuple[float, float]] = {}

    def add_parameter(self, name: str, low: float, high: float) -> None:
        """Add a parameter to the sensitivity analysis."""
        self.parameters[name] = (low, high)

    def analyze(
        self,
        objective_fn: Callable[[dict[str, float]], float],
    ) -> SobolResult:
        """Run Sobol sensitivity analysis using Saltelli sampling.

        Parameters
        ----------
        objective_fn : callable
            Model function mapping parameters to scalar output.

        Returns
        -------
        SobolResult
            First-order and total-order sensitivity indices.
        """
        names = list(self.parameters.keys())
        k = len(names)
        bounds = np.array([self.parameters[p] for p in names])

        # Generate Saltelli sample matrices
        A = self.rng.random((self.n_samples, k))
        B = self.rng.random((self.n_samples, k))

        # Scale to parameter bounds
        A_scaled = bounds[:, 0] + A * (bounds[:, 1] - bounds[:, 0])
        B_scaled = bounds[:, 0] + B * (bounds[:, 1] - bounds[:, 0])

        # Evaluate base matrices
        y_A = np.array([objective_fn(dict(zip(names, row))) for row in A_scaled])
        y_B = np.array([objective_fn(dict(zip(names, row))) for row in B_scaled])

        # Evaluate cross matrices (AB_i)
        first_order = np.zeros(k)
        total_order = np.zeros(k)

        for i in range(k):
            AB_i = B_scaled.copy()
            AB_i[:, i] = A_scaled[:, i]
            y_AB_i = np.array([objective_fn(dict(zip(names, row))) for row in AB_i])

            var_y = np.var(np.concatenate([y_A, y_B]))
            if var_y > 0:
                # Jansen estimators
                first_order[i] = np.mean(y_B * (y_AB_i - y_A)) / var_y
                total_order[i] = 0.5 * np.mean((y_A - y_AB_i) ** 2) / var_y

        logger.info("Sobol analysis complete for %d parameters", k)
        for i, name in enumerate(names):
            logger.info("  %s: S1=%.4f, ST=%.4f", name, first_order[i], total_order[i])

        return SobolResult(
            parameter_names=names,
            first_order=first_order,
            total_order=total_order,
            n_samples=self.n_samples,
        )

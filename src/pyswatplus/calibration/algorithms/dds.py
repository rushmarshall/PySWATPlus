"""Dynamically Dimensioned Search (DDS) algorithm.

Implements the DDS algorithm (Tolson & Shoemaker, 2007)
for automatic calibration of watershed models.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Callable

import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class DDSConfig:
    """DDS algorithm configuration."""

    max_iterations: int = 1000
    r_val: float = 0.2
    seed: int | None = None


@dataclass
class DDSResult:
    """DDS calibration result."""

    best_params: dict[str, float]
    best_objective: float
    history: list[dict[str, Any]] = field(default_factory=list)
    n_iterations: int = 0
    converged: bool = False


class DDSOptimizer:
    """Dynamically Dimensioned Search optimizer.

    DDS is a simple, efficient single-objective optimization algorithm
    that dynamically adjusts the search neighborhood. Early iterations
    explore globally; later iterations focus on refining the best solution.
    """

    def __init__(self, config: DDSConfig | None = None) -> None:
        self.config = config or DDSConfig()
        self.rng = np.random.default_rng(self.config.seed)

    def optimize(
        self,
        objective_fn: Callable[[dict[str, float]], float],
        parameter_bounds: dict[str, tuple[float, float]],
        maximize: bool = True,
    ) -> DDSResult:
        """Run DDS optimization.

        Parameters
        ----------
        objective_fn : callable
            Function that takes parameter dict, returns objective value.
        parameter_bounds : dict
            Parameter name to (min, max) bounds mapping.
        maximize : bool
            If True, maximize objective; if False, minimize.

        Returns
        -------
        DDSResult
            Optimization results with best parameters and history.
        """
        param_names = list(parameter_bounds.keys())
        n_params = len(param_names)
        bounds = np.array([parameter_bounds[p] for p in param_names])

        # Initialize with random point
        x_best = self.rng.uniform(bounds[:, 0], bounds[:, 1])
        params_best = dict(zip(param_names, x_best))
        f_best = objective_fn(params_best)

        history = [{"iteration": 0, "objective": f_best, "params": params_best.copy()}]
        logger.info("DDS initial: objective = %.6f", f_best)

        for i in range(1, self.config.max_iterations + 1):
            # Probability of perturbing each dimension
            p = 1.0 - np.log(i) / np.log(self.config.max_iterations)
            p = max(p, 1.0 / n_params)

            # Perturb selected dimensions
            x_new = x_best.copy()
            perturbed = self.rng.random(n_params) < p
            if not perturbed.any():
                perturbed[self.rng.integers(n_params)] = True

            for j in np.where(perturbed)[0]:
                sigma = self.config.r_val * (bounds[j, 1] - bounds[j, 0])
                x_new[j] = x_best[j] + self.rng.normal(0, sigma)
                x_new[j] = np.clip(x_new[j], bounds[j, 0], bounds[j, 1])

            params_new = dict(zip(param_names, x_new))
            f_new = objective_fn(params_new)

            improved = (f_new > f_best) if maximize else (f_new < f_best)
            if improved:
                x_best = x_new
                f_best = f_new
                params_best = params_new.copy()
                logger.debug("DDS iter %d: improved to %.6f", i, f_best)

            if i % 100 == 0:
                history.append({
                    "iteration": i,
                    "objective": f_best,
                    "params": params_best.copy(),
                })

        logger.info("DDS completed: best objective = %.6f after %d iterations", f_best, i)

        return DDSResult(
            best_params=params_best,
            best_objective=f_best,
            history=history,
            n_iterations=i,
            converged=True,
        )

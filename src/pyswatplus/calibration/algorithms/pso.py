"""Particle Swarm Optimization (PSO) algorithm.

Implements PSO with inertia weight for calibration of
hydrological models.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Callable

import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class PSOConfig:
    """PSO algorithm configuration."""

    n_particles: int = 30
    max_iterations: int = 500
    w: float = 0.7  # inertia weight
    c1: float = 1.5  # cognitive coefficient
    c2: float = 1.5  # social coefficient
    seed: int | None = None


@dataclass
class PSOResult:
    """PSO calibration result."""

    best_params: dict[str, float]
    best_objective: float
    history: list[dict[str, Any]] = field(default_factory=list)
    n_iterations: int = 0


class PSOOptimizer:
    """Particle Swarm Optimization for model calibration.

    Each particle represents a candidate parameter set that moves
    through the search space guided by its own best position and
    the global best position found by the swarm.
    """

    def __init__(self, config: PSOConfig | None = None) -> None:
        self.config = config or PSOConfig()
        self.rng = np.random.default_rng(self.config.seed)

    def optimize(
        self,
        objective_fn: Callable[[dict[str, float]], float],
        parameter_bounds: dict[str, tuple[float, float]],
        maximize: bool = True,
    ) -> PSOResult:
        """Run PSO optimization."""
        names = list(parameter_bounds.keys())
        n = len(names)
        bounds = np.array([parameter_bounds[p] for p in names])
        lo, hi = bounds[:, 0], bounds[:, 1]
        span = hi - lo

        # Initialize swarm
        positions = self.rng.uniform(lo, hi, (self.config.n_particles, n))
        velocities = self.rng.uniform(-span * 0.1, span * 0.1, (self.config.n_particles, n))

        # Evaluate initial positions
        scores = np.array([
            objective_fn(dict(zip(names, pos))) for pos in positions
        ])

        p_best_pos = positions.copy()
        p_best_scores = scores.copy()

        g_best_idx = int(np.argmax(scores) if maximize else np.argmin(scores))
        g_best_pos = positions[g_best_idx].copy()
        g_best_score = scores[g_best_idx]

        history = [{"iteration": 0, "objective": g_best_score}]

        for it in range(1, self.config.max_iterations + 1):
            r1 = self.rng.random((self.config.n_particles, n))
            r2 = self.rng.random((self.config.n_particles, n))

            velocities = (
                self.config.w * velocities
                + self.config.c1 * r1 * (p_best_pos - positions)
                + self.config.c2 * r2 * (g_best_pos - positions)
            )

            positions += velocities
            positions = np.clip(positions, lo, hi)

            scores = np.array([
                objective_fn(dict(zip(names, pos))) for pos in positions
            ])

            if maximize:
                improved = scores > p_best_scores
            else:
                improved = scores < p_best_scores

            p_best_pos[improved] = positions[improved]
            p_best_scores[improved] = scores[improved]

            best_idx = int(np.argmax(scores) if maximize else np.argmin(scores))
            if (maximize and scores[best_idx] > g_best_score) or \
               (not maximize and scores[best_idx] < g_best_score):
                g_best_pos = positions[best_idx].copy()
                g_best_score = scores[best_idx]

            if it % 50 == 0:
                history.append({"iteration": it, "objective": g_best_score})
                logger.debug("PSO iter %d: best = %.6f", it, g_best_score)

        return PSOResult(
            best_params=dict(zip(names, g_best_pos)),
            best_objective=g_best_score,
            history=history,
            n_iterations=it,
        )

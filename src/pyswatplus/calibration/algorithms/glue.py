"""Generalized Likelihood Uncertainty Estimation (GLUE).

Implements the GLUE methodology (Beven & Binley, 1992)
for uncertainty analysis in hydrological modeling.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Callable

import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class GLUEConfig:
    """GLUE analysis configuration."""

    n_simulations: int = 10000
    threshold: float = 0.5
    likelihood_measure: str = "nse"
    confidence_levels: tuple[float, float] = (0.05, 0.95)
    seed: int | None = None


@dataclass
class GLUEResult:
    """GLUE analysis result."""

    behavioral_params: list[dict[str, float]]
    behavioral_scores: np.ndarray
    acceptance_rate: float
    prediction_bounds: dict[str, np.ndarray] | None = None
    dotty_data: dict[str, Any] = field(default_factory=dict)


class GLUEAnalyzer:
    """GLUE uncertainty estimation.

    Performs Monte Carlo sampling of the parameter space,
    identifies behavioral parameter sets above a threshold,
    and constructs prediction uncertainty bounds.
    """

    def __init__(self, config: GLUEConfig | None = None) -> None:
        self.config = config or GLUEConfig()
        self.rng = np.random.default_rng(self.config.seed)

    def analyze(
        self,
        objective_fn: Callable[[dict[str, float]], float],
        parameter_bounds: dict[str, tuple[float, float]],
    ) -> GLUEResult:
        """Run GLUE analysis.

        Parameters
        ----------
        objective_fn : callable
            Function mapping parameters to likelihood value.
        parameter_bounds : dict
            Parameter bounds for Monte Carlo sampling.

        Returns
        -------
        GLUEResult
            Behavioral parameters and uncertainty bounds.
        """
        names = list(parameter_bounds.keys())
        bounds = np.array([parameter_bounds[p] for p in names])

        # Monte Carlo sampling
        all_params = []
        all_scores = []

        for i in range(self.config.n_simulations):
            sample = self.rng.uniform(bounds[:, 0], bounds[:, 1])
            params = dict(zip(names, sample))
            score = objective_fn(params)
            all_params.append(params)
            all_scores.append(score)

            if (i + 1) % 1000 == 0:
                logger.debug("GLUE: %d/%d simulations", i + 1, self.config.n_simulations)

        scores = np.array(all_scores)

        # Identify behavioral simulations
        behavioral_mask = scores >= self.config.threshold
        behavioral_params = [p for p, m in zip(all_params, behavioral_mask) if m]
        behavioral_scores = scores[behavioral_mask]

        acceptance_rate = len(behavioral_params) / self.config.n_simulations

        logger.info(
            "GLUE: %d/%d behavioral (%.1f%%), threshold=%.2f",
            len(behavioral_params),
            self.config.n_simulations,
            acceptance_rate * 100,
            self.config.threshold,
        )

        # Dotty plot data
        dotty = {}
        for name in names:
            dotty[name] = {
                "values": [p[name] for p in all_params],
                "scores": scores.tolist(),
            }

        return GLUEResult(
            behavioral_params=behavioral_params,
            behavioral_scores=behavioral_scores,
            acceptance_rate=acceptance_rate,
            dotty_data=dotty,
        )

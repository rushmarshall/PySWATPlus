"""Objective function library for model calibration.

Implements standard hydrological performance metrics
following Moriasi et al. (2007, 2015) guidelines.
"""

from __future__ import annotations

import numpy as np
from typing import Callable

ObjectiveFunction = Callable[[np.ndarray, np.ndarray], float]


def nse(observed: np.ndarray, simulated: np.ndarray) -> float:
    """Nash-Sutcliffe Efficiency (Nash & Sutcliffe, 1970).

    Range: (-inf, 1], Optimal: 1.0
    NSE > 0.5 is generally acceptable for watershed modeling.
    """
    numerator = np.sum((observed - simulated) ** 2)
    denominator = np.sum((observed - np.mean(observed)) ** 2)
    if denominator == 0:
        return -np.inf
    return 1.0 - numerator / denominator


def kge(observed: np.ndarray, simulated: np.ndarray) -> float:
    """Kling-Gupta Efficiency (Gupta et al., 2009).

    Decomposes into correlation, bias ratio, and variability ratio.
    Range: (-inf, 1], Optimal: 1.0
    """
    r = np.corrcoef(observed, simulated)[0, 1] if len(observed) > 1 else 0
    alpha = np.std(simulated) / np.std(observed) if np.std(observed) > 0 else 0
    beta = np.mean(simulated) / np.mean(observed) if np.mean(observed) > 0 else 0
    return 1.0 - np.sqrt((r - 1) ** 2 + (alpha - 1) ** 2 + (beta - 1) ** 2)


def pbias(observed: np.ndarray, simulated: np.ndarray) -> float:
    """Percent Bias (Gupta et al., 1999).

    Range: (-inf, inf), Optimal: 0.0
    |PBIAS| < 25% is generally acceptable.
    """
    total = np.sum(observed)
    if total == 0:
        return np.inf
    return 100.0 * np.sum(simulated - observed) / total


def rmse(observed: np.ndarray, simulated: np.ndarray) -> float:
    """Root Mean Square Error.

    Range: [0, inf), Optimal: 0.0
    """
    return float(np.sqrt(np.mean((observed - simulated) ** 2)))


def r_squared(observed: np.ndarray, simulated: np.ndarray) -> float:
    """Coefficient of Determination.

    Range: [0, 1], Optimal: 1.0
    """
    r = np.corrcoef(observed, simulated)[0, 1] if len(observed) > 1 else 0
    return float(r ** 2)


def log_nse(observed: np.ndarray, simulated: np.ndarray) -> float:
    """Log-transformed NSE for low-flow emphasis.

    Applies log transformation before computing NSE.
    """
    eps = 1e-6
    log_obs = np.log(np.maximum(observed, eps))
    log_sim = np.log(np.maximum(simulated, eps))
    return nse(log_obs, log_sim)


OBJECTIVE_REGISTRY: dict[str, ObjectiveFunction] = {
    "nse": nse,
    "kge": kge,
    "pbias": pbias,
    "rmse": rmse,
    "r2": r_squared,
    "log_nse": log_nse,
}


def get_objective(name: str) -> ObjectiveFunction:
    """Retrieve an objective function by name."""
    if name not in OBJECTIVE_REGISTRY:
        raise ValueError(f"Unknown objective: {name}. Available: {list(OBJECTIVE_REGISTRY)}")
    return OBJECTIVE_REGISTRY[name]

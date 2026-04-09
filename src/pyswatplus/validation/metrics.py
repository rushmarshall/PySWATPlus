"""Statistical validation metrics and tests.

Provides split-sample validation, multi-site assessment,
and performance rating following Moriasi et al. (2015).
"""

from __future__ import annotations

import numpy as np

from pyswatplus.calibration.objective import nse, kge, pbias, rmse, r_squared


def performance_rating(metric_name: str, value: float) -> str:
    """Rate model performance following Moriasi et al. (2015).

    Parameters
    ----------
    metric_name : str
        One of: nse, kge, pbias, r2
    value : float
        The metric value to rate.

    Returns
    -------
    str
        Rating: "Very Good", "Good", "Satisfactory", or "Unsatisfactory"
    """
    ratings = {
        "nse": [(0.75, "Very Good"), (0.65, "Good"), (0.50, "Satisfactory")],
        "kge": [(0.75, "Very Good"), (0.50, "Good"), (0.00, "Satisfactory")],
        "r2": [(0.85, "Very Good"), (0.75, "Good"), (0.60, "Satisfactory")],
    }

    if metric_name == "pbias":
        abs_val = abs(value)
        if abs_val < 10:
            return "Very Good"
        elif abs_val < 15:
            return "Good"
        elif abs_val < 25:
            return "Satisfactory"
        return "Unsatisfactory"

    thresholds = ratings.get(metric_name)
    if thresholds is None:
        return "N/A"

    for threshold, rating in thresholds:
        if value >= threshold:
            return rating
    return "Unsatisfactory"


def compute_all_metrics(observed: np.ndarray, simulated: np.ndarray) -> dict[str, float]:
    """Compute all standard hydrological metrics."""
    return {
        "NSE": nse(observed, simulated),
        "KGE": kge(observed, simulated),
        "PBIAS": pbias(observed, simulated),
        "RMSE": rmse(observed, simulated),
        "R2": r_squared(observed, simulated),
    }

"""Tests for DDS optimizer."""
import numpy as np
from pyswatplus.calibration.algorithms.dds import DDSOptimizer, DDSConfig


def test_dds_converges():
    """DDS should find the minimum of a simple quadratic."""
    def sphere(params):
        return -sum(v**2 for v in params.values())

    opt = DDSOptimizer(DDSConfig(max_iterations=200, seed=42))
    result = opt.optimize(
        sphere,
        {"x": (-5.0, 5.0), "y": (-5.0, 5.0)},
        maximize=True,
    )
    assert result.best_objective > -1.0
    assert abs(result.best_params["x"]) < 2.0
    assert abs(result.best_params["y"]) < 2.0

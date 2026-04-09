"""Tests for validation metrics."""
from pyswatplus.validation.metrics import performance_rating, compute_all_metrics
import numpy as np


def test_rating_nse():
    assert performance_rating("nse", 0.80) == "Very Good"
    assert performance_rating("nse", 0.70) == "Good"
    assert performance_rating("nse", 0.55) == "Satisfactory"
    assert performance_rating("nse", 0.30) == "Unsatisfactory"


def test_rating_pbias():
    assert performance_rating("pbias", 5.0) == "Very Good"
    assert performance_rating("pbias", -30.0) == "Unsatisfactory"


def test_compute_all():
    obs = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    sim = obs + np.array([0.1, -0.1, 0.2, -0.1, 0.0])
    metrics = compute_all_metrics(obs, sim)
    assert "NSE" in metrics
    assert "KGE" in metrics
    assert metrics["NSE"] > 0.9

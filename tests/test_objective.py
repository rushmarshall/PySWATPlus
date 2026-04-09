"""Tests for objective functions."""
import numpy as np
import pytest
from pyswatplus.calibration.objective import nse, kge, pbias, rmse, r_squared, log_nse, get_objective


def test_nse_perfect():
    obs = np.array([1.0, 2.0, 3.0, 4.0])
    assert nse(obs, obs) == pytest.approx(1.0)


def test_nse_mean():
    obs = np.array([1.0, 2.0, 3.0, 4.0])
    sim = np.full_like(obs, obs.mean())
    assert nse(obs, sim) == pytest.approx(0.0)


def test_kge_perfect():
    obs = np.array([1.0, 2.0, 3.0, 4.0])
    assert kge(obs, obs) == pytest.approx(1.0)


def test_pbias_zero():
    obs = np.array([1.0, 2.0, 3.0])
    assert pbias(obs, obs) == pytest.approx(0.0)


def test_rmse_zero():
    obs = np.array([1.0, 2.0, 3.0])
    assert rmse(obs, obs) == pytest.approx(0.0)


def test_r_squared_perfect():
    obs = np.array([1.0, 2.0, 3.0, 4.0])
    assert r_squared(obs, obs) == pytest.approx(1.0)


def test_get_objective_invalid():
    with pytest.raises(ValueError):
        get_objective("invalid")

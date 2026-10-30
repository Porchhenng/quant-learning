"""Run with: pytest  (all of these fail until you write src/quant/metrics.py)"""

import numpy as np
import pandas as pd
import pytest

from quant import metrics


def test_total_return_compounds():
    r = pd.Series([0.10, 0.10])
    assert metrics.total_return(r) == pytest.approx(0.21)


def test_annual_return_one_year_flat_growth():
    r = pd.Series([0.001] * 252)
    assert metrics.annual_return(r) == pytest.approx(1.001**252 - 1)


def test_annual_return_two_years_same_speed():
    # Same daily growth for 2 years: total doubles up, but the yearly rate stays the same
    r = pd.Series([0.001] * 504)
    assert metrics.annual_return(r) == pytest.approx(1.001**252 - 1)


def test_annual_volatility_scales_by_sqrt_252():
    r = pd.Series([0.01, -0.01] * 126)
    assert metrics.annual_volatility(r) == pytest.approx(r.std() * np.sqrt(252))


def test_sharpe_is_return_over_volatility():
    r = pd.Series([0.002, -0.001] * 126)
    expected = metrics.annual_return(r) / metrics.annual_volatility(r)
    assert metrics.sharpe_ratio(r) == pytest.approx(expected)


def test_max_drawdown_finds_worst_fall():
    # 100 -> 110 -> 88 -> 99: worst fall is 110 -> 88 = -20%
    r = pd.Series([0.10, -0.20, 0.125])
    assert metrics.max_drawdown(r) == pytest.approx(-0.20)


def test_max_drawdown_is_zero_when_only_rising():
    assert metrics.max_drawdown(pd.Series([0.01, 0.02, 0.03])) == pytest.approx(0.0)

"""Performance measures for M3. Write these yourself; tests/test_metrics.py checks them.

Every function takes a Series of DAILY returns (0.01 = +1%).
Use 252 trading days per year.
"""

import pandas as pd
import numpy as np
TRADING_DAYS = 252


def total_return(returns: pd.Series) -> float:
    """Growth over the whole period. +10% then +10% is 0.21, not 0.20."""
    return (1 + returns).prod() - 1


def annual_return(returns: pd.Series) -> float:
    """Compound growth per year (CAGR)."""
    growth =  1 + total_return(returns)
    year = len(returns) / TRADING_DAYS

    return growth ** (1 / year) - 1

def annual_volatility(returns: pd.Series) -> float:
    """Standard deviation of daily returns, scaled to a year."""
    daily_volume = returns.std()
    var2 = np.sqrt(TRADING_DAYS)
    return daily_volume * var2


def sharpe_ratio(returns: pd.Series) -> float:
    """Yearly return / yearly volatility. Assume a 0% risk-free rate."""
    return annual_return(returns) / annual_volatility(returns)


def max_drawdown(returns: pd.Series) -> float:
    """Biggest fall from a previous peak, as a negative number (-0.25 = -25%)."""
    raise NotImplementedError

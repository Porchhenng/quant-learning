"""Download daily prices once, then reuse the saved copy in data/."""

import warnings
from pathlib import Path

import pandas as pd
import yfinance as yf

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_prices(ticker: str = "GC=F", start: str = "2010-01-01", refresh: bool = False) -> pd.Series:
    """Daily closing prices for one ticker. GC=F is gold futures; GLD is the gold ETF."""
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / f"{ticker.replace('=', '_')}_{start}.csv"
    if path.exists() and not refresh:
        return pd.read_csv(path, index_col=0, parse_dates=True).iloc[:, 0]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # yfinance's pandas deprecation noise
        df = yf.download(ticker, start=start, auto_adjust=True, progress=False)
    close = df["Close"].squeeze().dropna()
    close.name = ticker
    close.to_csv(path)
    return close

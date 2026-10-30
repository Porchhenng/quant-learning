# Quant Learning

Learning quant basics by building and honestly testing a gold trading strategy. No real money: everything is tested on past data.

Milestones and progress live in the Obsidian vault: `projects/quant-learning/_index.md`.

## Setup

```sh
cd ~/Developer/personal/quant-learning
source .venv/bin/activate
jupyter lab            # opens the notebooks in the browser
pytest                 # checks src/quant/metrics.py
```

## Layout

| Path | What |
|---|---|
| `notebooks/00-gold-chart.ipynb` | M0: download gold, plot it, M1 warm-ups |
| `notebooks/03-ma-crossover.ipynb` | M3–M4: the first backtest, with TODOs |
| `src/quant/data.py` | `load_prices()`: downloads once, then reads the copy in `data/` |
| `src/quant/metrics.py` | Return, volatility, Sharpe, drawdown. **You write these** |
| `tests/test_metrics.py` | Known answers for the metrics |
| `data/` | Downloaded prices (not committed) |

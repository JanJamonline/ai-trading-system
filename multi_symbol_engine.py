import pandas as pd
from backtest_engine.backtest_engine import BacktestEngine


def generate_signals_multi(symbols: list[str]) -> pd.DataFrame:
    all_results = []

    for symbol in symbols:
        engine = BacktestEngine(symbol)
        df = engine.run()
        all_results.append(df)

    return pd.concat(all_results, ignore_index=True)

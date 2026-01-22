import pandas as pd

from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from backtest_engine.backtest_engine import BacktestEngine


def generate_signals_multi(symbols):
    all_results = []

    for symbol in symbols:
        df = pd.read_csv(f"data/{symbol}_5m.csv")
        df.columns = [c.lower() for c in df.columns]

        ta_5m = TAManager(df)
        fa = FAManager()

        engine = BacktestEngine(
            ta_5m=ta_5m,
            fa=fa
        )

        all_results.extend(engine.run(df, symbol))

    return pd.DataFrame(all_results)

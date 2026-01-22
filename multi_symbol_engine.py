import pandas as pd

from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from backtest_engine.backtest_engine import BacktestEngine


def generate_signals_multi(symbols):
    all_results = []

    for symbol in symbols:
        df_5m = pd.read_csv(f"data/{symbol}_5m.csv")

        # Initialize modules
        ta_5m = TAManager(df_5m)
        fa = FAManager("data/fa_data.csv")

        # Engine MUST be created with dependencies
        engine = BacktestEngine(
            ta_5m=ta_5m,
            fa=fa
        )

        results = engine.run(df_5m, symbol)
        all_results.extend(results)

    return all_results

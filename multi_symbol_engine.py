import pandas as pd

from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from signal_fusion.fusion_engine import FusionEngine
from backtest_engine.backtest_engine import BacktestEngine


def generate_signals_multi(symbols):
    all_results = []

    for symbol in symbols:
        price_path = f"data/{symbol}_5m.csv"
        price_df = pd.read_csv(price_path)

        ta = TAManager(price_df)
        fa = FAManager("data/fa_data.csv")
        fusion = FusionEngine()

        engine = BacktestEngine(ta, fa, fusion)
        results = engine.run(price_df, symbol)

        all_results.extend(results)

    return all_results

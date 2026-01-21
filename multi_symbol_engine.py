import pandas as pd
from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from signal_fusion.fusion_engine import FusionEngine
from backtest_engine.backtest_engine import BacktestEngine

def generate_signals_multi(symbols):
    all_results = []

    for symbol in symbols:
        price_path = f"data/{symbol}_5m.csv"
        fa_path = "data/fa_data.csv"

        price_df = pd.read_csv(price_path)
        fa_df = pd.read_csv(fa_path)

        ta = TAManager(price_df)          # ✅ FIXED
        fa = FAManager(fa_df)
        fusion = FusionEngine()

        engine = BacktestEngine(ta, fa, fusion)
        all_results.extend(engine.run(price_df, symbol))

    return all_results

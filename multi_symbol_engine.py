import pandas as pd
from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from signal_fusion.fusion_engine import FusionEngine
from backtest_engine.backtest_engine import BacktestEngine

def generate_signals_multi(symbols):
    ta = TAManager()
    fa = FAManager()
    fusion = FusionEngine()
    engine = BacktestEngine(ta, fa, fusion)

    all_results = []

    for symbol in symbols:
        df = pd.read_csv(f"data/{symbol}_5m.csv")
        all_results.extend(engine.run(df, symbol))

    return all_results

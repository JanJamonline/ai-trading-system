# multi_symbol_engine.py

import pandas as pd

from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from signal_fusion.fusion_engine import FusionEngine
from backtest_engine.backtest_engine import BacktestEngine
from timeframe_engine.timeframe_validator import TimeframeValidator


def safe_read_csv(path):
    try:
        df = pd.read_csv(path)
        if df.empty:
            return None
        return df
    except Exception:
        return None


def generate_signals_multi(symbols):
    all_results = []

    for symbol in symbols:
        df_5m = safe_read_csv(f"data/{symbol}_5m.csv")
        df_15m = safe_read_csv(f"data/{symbol}_15m.csv")

        if df_5m is None:
            raise ValueError(f"Missing or empty 5m data for {symbol}")

        ta_5m = TAManager(df_5m)
        ta_15m = TAManager(df_15m) if df_15m is not None else None

        fa = FAManager("data/fa_data.csv")
        fusion = FusionEngine()
        tf_validator = TimeframeValidator()

        engine = BacktestEngine(
            ta_5m=ta_5m,
            ta_15m=ta_15m,
            fa=fa,
            fusion=fusion,
            tf_validator=tf_validator
        )

        all_results.extend(engine.run(df_5m, symbol))

    return all_results

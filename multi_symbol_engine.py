# multi_symbol_engine.py

from backtest_engine.backtest_engine import BacktestEngine
from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from price_module.live_price_manager import LivePriceManager


def generate_signals_multi(symbols):
    """
    Generates signals for multiple symbols using:
    - Live price data
    - TA manager
    - FA manager
    - Backtest engine (fusion handled internally)
    """

    all_results = []

    for symbol in symbols:
        print(f"Fetching LIVE data for {symbol}")

        # --- PRICE DATA ---
        price_manager = LivePriceManager(symbol)
        df_5m = price_manager.fetch(interval="5m")

        # --- TA & FA ---
        ta_5m = TAManager(df_5m)
        fa = FAManager()

        # ✅ CORRECT CONSTRUCTOR (NO fusion= HERE)
        engine = BacktestEngine(
            ta_5m=ta_5m,
            fa=fa
        )

        results = engine.run(df_5m, symbol)
        all_results.extend(results)

    return all_results

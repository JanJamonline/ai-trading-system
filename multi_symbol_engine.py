from backtest_engine.backtest_engine import BacktestEngine
from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from signal_fusion.fusion_engine import FusionEngine
from price_module.live_price_manager import LivePriceManager


def generate_signals_multi(symbols):
    all_results = []

    for symbol in symbols:
        print(f"Fetching LIVE data for {symbol}")

        price_manager = LivePriceManager(symbol)
        df_5m = price_manager.fetch(interval="5m")

        ta_5m = TAManager(df_5m)
        fa = FAManager()
        fusion = FusionEngine()

        engine = BacktestEngine(
            ta_5m=ta_5m,
            fa=fa,
            fusion=fusion
        )

        all_results.extend(engine.run(df_5m, symbol))

    return all_results

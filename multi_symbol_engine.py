from backtest_engine.backtest_engine import BacktestEngine
from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from signal_fusion.fusion_engine import FusionEngine
from price_module.live_price_manager import LivePriceManager

def generate_signals_multi(symbols):
    all_results = []

    for symbol in symbols:
        price_manager = LivePriceManager(symbol)
        df = price_manager.fetch(interval="5m")

        ta_manager = TAManager(df)
        fa_manager = FAManager()
        fusion_engine = FusionEngine()

        engine = BacktestEngine(
            ta_manager=ta_manager,
            fa_manager=fa_manager,
            fusion_engine=fusion_engine
        )

        all_results.extend(engine.run(df, symbol))

    return all_results

from price_module.live_price_manager import LivePriceManager
from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from backtest_engine.backtest_engine import BacktestEngine

def generate_signals_multi(symbols):
    all_results = []

    for symbol in symbols:
        price_manager = LivePriceManager(symbol)
        df = price_manager.fetch(interval="5m")

        ta = TAManager(df)
        fa = FAManager()

        engine = BacktestEngine(
            ta_manager=ta,
            fa_manager=fa
        )

        all_results.extend(engine.run(df, symbol))

    return all_results

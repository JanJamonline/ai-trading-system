from price_module.price_manager import PriceManager
from ta_module.ta_manager import TAManager
from decision_engine.decision_engine import DecisionEngine
from backtest_engine.backtest_engine import BacktestEngine

def generate_signals_multi(symbols):
    all_results = []

    for symbol in symbols:
        csv_path = f"data/{symbol}_5m.csv"

        price_manager = PriceManager(csv_path=csv_path, symbol=symbol)
        ta_manager = TAManager()
        decision_engine = DecisionEngine()

        engine = BacktestEngine(
            price_manager=price_manager,
            ta_manager=ta_manager,
            decision_engine=decision_engine,
            symbol=symbol
        )

        results = engine.run()
        all_results.extend(results)

    return all_results

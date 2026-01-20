from price_module.price_manager import PriceManager
from ta_module.ta_manager import TAManager
from decision_engine.decision_engine import DecisionEngine
from backtest_engine.backtest_engine import BacktestEngine

def generate_signals():
    price_manager = PriceManager("data/sample_prices.csv")
    prices_df = price_manager.get_prices()

    ta_manager = TAManager()
    decision_engine = DecisionEngine()

    engine = BacktestEngine(prices_df, ta_manager, decision_engine)
    return engine.run()

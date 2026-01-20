import pandas as pd
from price_module.price_manager import PriceManager
from ta_module.ta_manager import TAManager
from decision_engine.decision_engine import DecisionEngine


class BacktestEngine:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.ta = TAManager()
        self.decision = DecisionEngine()

    def run(self) -> pd.DataFrame:
        pm = PriceManager("data/sample_prices.csv", self.symbol)
        prices = pm.get_prices()

        ta_df = self.ta.compute(prices)
        final_df = self.decision.evaluate(ta_df)

        return final_df

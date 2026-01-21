class BacktestEngine:
    def __init__(self, price_manager, ta_manager, decision_engine, symbol):
        self.price_manager = price_manager
        self.ta = ta_manager
        self.decision = decision_engine
        self.symbol = symbol

        print("BacktestEngine initialized")

    def run(self):
        prices_df = self.price_manager.load_prices()
        prices_df = self.ta.compute(prices_df)

        results = []

        for i, row in prices_df.iterrows():
            decision = self.decision.evaluate(row)

            results.append({
                "time": row.get("time", i),
                "symbol": self.symbol,
                "price": row["close"],
                **decision
            })

        return results

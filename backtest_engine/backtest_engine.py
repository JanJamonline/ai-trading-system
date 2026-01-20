class BacktestEngine:
    def __init__(self, price_manager, ta_manager, decision_engine, symbol):
        self.price = price_manager
        self.ta = ta_manager
        self.decision = decision_engine
        self.symbol = symbol
        print("BacktestEngine initialized")

    def run(self):
        prices_df = self.price.get_prices()
        prices_df = self.ta.compute(prices_df)

        results = []

        for i in range(len(prices_df)):
            signal, direction, confidence, reason = self.decision.evaluate(
                prices_df.iloc[i]
            )

            results.append({
                "time": prices_df.iloc[i]["time"],
                "symbol": self.symbol,
                "price": prices_df.iloc[i]["close"],
                "signal": signal,
                "direction": direction,
                "confidence": confidence,
                "reason": reason
            })

        return results

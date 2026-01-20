class BacktestEngine:
    def __init__(self, prices_df, ta_manager, decision_engine):
        self.prices_df = prices_df
        self.ta = ta_manager
        self.decision = decision_engine

    def run(self):
        results = []

        prices = self.prices_df["price"].tolist()

        for i in range(len(prices)):
            ta_signal = self.ta.compute(prices, i)
            signal, direction, confidence = self.decision.evaluate(ta_signal)

            results.append({
                "time": self.prices_df.iloc[i]["time"],
                "symbol": self.prices_df.iloc[i]["symbol"],
                "price": prices[i],
                "signal": signal,
                "direction": direction,
                "confidence": confidence,
                "reason": ta_signal
            })

        return results

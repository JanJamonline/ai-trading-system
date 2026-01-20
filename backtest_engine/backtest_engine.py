class BacktestEngine:
    def __init__(self, price_manager, ta_manager, decision_engine, symbol):
        self.price = price_manager
        self.ta = ta_manager
        self.decision = decision_engine
        self.symbol = symbol

        print("BacktestEngine initialized")

    def run(self):
        prices_df = self.price.get_prices()
        results = []

        last_ta_signal = None
        confirmation_count = 0

        for i in range(1, len(prices_df)):
            ta_signal = self.ta.compute(
                prices_df.iloc[i],
                prices_df.iloc[i - 1]
            )

            # 3️⃣ Trend Confirmation (2 candles)
            if ta_signal["signal"] == last_ta_signal:
                confirmation_count += 1
            else:
                confirmation_count = 1

            last_ta_signal = ta_signal["signal"]

            if confirmation_count < 2:
                decision = {
                    "signal": "HOLD",
                    "direction": "NEUTRAL",
                    "confidence": 0,
                    "reason": "NO_CONFIRMATION"
                }
            else:
                decision = self.decision.evaluate(i, ta_signal)

            results.append({
                "time": prices_df.iloc[i]["time"],
                "symbol": self.symbol,
                "price": prices_df.iloc[i]["close"],
                "signal": decision["signal"],
                "direction": decision["direction"],
                "confidence": decision["confidence"],
                "reason": decision["reason"]
            })

        return results

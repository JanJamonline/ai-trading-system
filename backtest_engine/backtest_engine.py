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

        last_signal = None
        confirmation = 0

        for i in range(1, len(prices_df)):
            ta_signal = self.ta.compute(
                prices_df.iloc[i],
                prices_df.iloc[i - 1]
            )

            if ta_signal["signal"] == last_signal:
                confirmation += 1
            else:
                confirmation = 1

            last_signal = ta_signal["signal"]

            if confirmation < 2:
                decision = {
                    "signal": "HOLD",
                    "direction": "NEUTRAL",
                    "confidence": 0,
                    "signal_strength": "WEAK",
                    "risk_label": "HIGH_RISK",
                    "exposure_hint": "IGNORE",
                    "reason": "NO_CONFIRMATION"
                }
            else:
                decision = self.decision.evaluate(ta_signal)

            results.append({
                "time": prices_df.iloc[i]["time"],
                "symbol": self.symbol,
                "price": prices_df.iloc[i]["close"],
                "signal": decision["signal"],
                "direction": decision["direction"],
                "confidence": decision["confidence"],
                "signal_strength": decision["signal_strength"],
                "risk_label": decision["risk_label"],
                "exposure_hint": decision["exposure_hint"],
                "reason": decision["reason"]
            })

        return results

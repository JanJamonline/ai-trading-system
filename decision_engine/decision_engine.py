class DecisionEngine:
    def __init__(self):
        print("DecisionEngine initialized")

    def evaluate(self, row):
        ta = row["ta_signal"]

        if ta == "UP":
            return {
                "signal": "BUY",
                "direction": "BULLISH",
                "confidence": 70,
                "reason": "UP"
            }
        elif ta == "DOWN":
            return {
                "signal": "SELL",
                "direction": "BEARISH",
                "confidence": 70,
                "reason": "DOWN"
            }
        else:
            return {
                "signal": "HOLD",
                "direction": "NEUTRAL",
                "confidence": 0,
                "reason": "NO_CONFIRMATION"
            }

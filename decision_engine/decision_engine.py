class DecisionEngine:
    def __init__(self):
        print("DecisionEngine initialized")

    def evaluate(self, row):
        trend = row["trend"]

        if trend == "UP":
            return ("BUY", "BULLISH", 70, "UP")
        elif trend == "DOWN":
            return ("SELL", "BEARISH", 70, "DOWN")
        else:
            return ("HOLD", "NEUTRAL", 0, "FLAT")

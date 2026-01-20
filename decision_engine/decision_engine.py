class DecisionEngine:
    def evaluate(self, ta_signal):
        if ta_signal == "UP":
            return ("BUY", "BULLISH", 70)
        elif ta_signal == "DOWN":
            return ("SELL", "BEARISH", 70)
        else:
            return ("HOLD", "NEUTRAL", 0)

class DecisionEngine:
    def __init__(self):
        print("DecisionEngine initialized")

    def evaluate(self, row):
        ta = row["ta_signal"]

        if ta == "UP":
            confidence = 70
            signal = "BUY"
            direction = "BULLISH"
            reason = "UP"
        elif ta == "DOWN":
            confidence = 70
            signal = "SELL"
            direction = "BEARISH"
            reason = "DOWN"
        else:
            confidence = 0
            signal = "HOLD"
            direction = "NEUTRAL"
            reason = "NO_CONFIRMATION"

        # 🔹 FINAL SIGNAL QUALITY (OPTION A)
        if confidence >= 70:
            quality = "STRONG"
        elif confidence >= 40:
            quality = "MEDIUM"
        else:
            quality = "WEAK"

        return {
            "signal": signal,
            "direction": direction,
            "confidence": confidence,
            "quality": quality,
            "reason": reason
        }

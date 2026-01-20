class DecisionEngine:
    def __init__(self, min_confidence=60, cooldown_candles=2):
        self.min_confidence = min_confidence
        self.cooldown_candles = cooldown_candles
        self.last_signal = None
        self.last_signal_index = -999

        print("DecisionEngine initialized")

    def evaluate(self, index, ta_signal):
        signal = ta_signal["signal"]
        direction = ta_signal["direction"]
        confidence = ta_signal["confidence"]
        reason = ta_signal["reason"]

        # 1️⃣ Confidence Gate
        if confidence < self.min_confidence:
            return {
                "signal": "HOLD",
                "direction": "NEUTRAL",
                "confidence": 0,
                "reason": "LOW_CONFIDENCE"
            }

        # 2️⃣ Cooldown Gate
        if self.last_signal is not None:
            if signal != self.last_signal:
                if index - self.last_signal_index < self.cooldown_candles:
                    return {
                        "signal": "HOLD",
                        "direction": "NEUTRAL",
                        "confidence": 0,
                        "reason": "COOLDOWN"
                    }

        # Accept signal
        self.last_signal = signal
        self.last_signal_index = index

        return {
            "signal": signal,
            "direction": direction,
            "confidence": confidence,
            "reason": reason
        }

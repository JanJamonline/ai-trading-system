class DecisionEngine:
    def __init__(self, min_confidence=60):
        self.min_confidence = min_confidence
        print("DecisionEngine initialized")

    def _strength_mapping(self, confidence):
        if confidence >= 80:
            return "STRONG", "LOW_RISK", "NORMAL"
        elif confidence >= 65:
            return "MEDIUM", "MEDIUM_RISK", "SMALL"
        else:
            return "WEAK", "HIGH_RISK", "IGNORE"

    def evaluate(self, ta_signal):
        confidence = ta_signal["confidence"]

        if confidence < self.min_confidence:
            return {
                "signal": "HOLD",
                "direction": "NEUTRAL",
                "confidence": 0,
                "signal_strength": "WEAK",
                "risk_label": "HIGH_RISK",
                "exposure_hint": "IGNORE",
                "reason": "LOW_CONFIDENCE"
            }

        strength, risk, exposure = self._strength_mapping(confidence)

        return {
            "signal": ta_signal["signal"],
            "direction": ta_signal["direction"],
            "confidence": confidence,
            "signal_strength": strength,
            "risk_label": risk,
            "exposure_hint": exposure,
            "reason": ta_signal["reason"]
        }

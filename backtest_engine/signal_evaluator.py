class SignalEvaluator:
    def evaluate_quality(self, signal_data):
        signal = signal_data["signal"]
        direction = signal_data["direction"]
        confidence = signal_data["confidence"]
        reason = signal_data["reason"]
        risk_label = signal_data["risk_label"]

        # STRONG
        if (
            signal in ["BUY", "SELL"]
            and direction != "NEUTRAL"
            and confidence >= 70
            and reason != "NO_CONFIRMATION"
            and risk_label != "HIGH_RISK"
        ):
            return "STRONG"

        # MEDIUM
        if signal in ["BUY", "SELL"] and confidence >= 50:
            return "MEDIUM"

        # WEAK
        return "WEAK"

class FusionEngine:
    """
    Combines TA + FA signals into:
    - fused signal
    - confidence quality
    - risk label
    """

    def fuse(self, ta_signal, ta_strength, fa_signal, fa_strength):
        # Default values
        signal = "HOLD"
        quality = "WEAK"
        risk = "HIGH_RISK"

        if ta_signal == fa_signal and ta_signal in ["BUY", "SELL"]:
            signal = ta_signal
            quality = "STRONG" if ta_strength >= 70 and fa_strength >= 70 else "MEDIUM"
            risk = "LOW_RISK" if quality == "STRONG" else "MEDIUM_RISK"

        return signal, quality, risk

    def final_action(self, signal, quality, risk):
        if signal == "BUY" and quality == "STRONG" and risk == "LOW_RISK":
            return "BUY"
        if signal == "SELL" and quality == "STRONG" and risk == "LOW_RISK":
            return "SELL"
        return "WAIT"

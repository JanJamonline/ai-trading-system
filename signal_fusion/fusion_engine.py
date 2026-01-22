class FusionEngine:
    """
    Combines TA and FA signals into a final actionable signal.
    """

    def fuse(self, ta_signal: str, fa_signal: str):
        # Default
        signal = "HOLD"
        quality = "WEAK"
        risk_label = "HIGH_RISK"

        if ta_signal == "BUY" and fa_signal == "BULLISH":
            signal = "BUY"
            quality = "STRONG"
            risk_label = "LOW_RISK"

        elif ta_signal == "SELL" and fa_signal == "BEARISH":
            signal = "SELL"
            quality = "STRONG"
            risk_label = "LOW_RISK"

        elif ta_signal in ["BUY", "SELL"]:
            signal = "HOLD"
            quality = "WEAK"
            risk_label = "MEDIUM_RISK"

        return signal, quality, risk_label

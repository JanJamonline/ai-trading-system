class FusionEngine:
    def combine(self, ta_signal, ta_strength, fa_signal, fa_strength):
        # Base combined signal
        if ta_signal == "BUY" and fa_signal == "BULLISH":
            signal = "BUY"
            quality = "STRONG"
        elif ta_signal == "SELL" and fa_signal == "BEARISH":
            signal = "SELL"
            quality = "STRONG"
        elif ta_signal in ["BUY", "SELL"]:
            signal = "HOLD"
            quality = "WEAK"
        else:
            signal = "HOLD"
            quality = "WEAK"

        # Action column (final trader-facing instruction)
        if signal == "BUY" and quality == "STRONG":
            action = "BUY"
        elif signal == "SELL" and quality == "STRONG":
            action = "SELL"
        elif signal in ["BUY", "SELL"] and quality == "MEDIUM":
            action = signal
        else:
            action = "WAIT"

        return {
            "signal": signal,
            "quality": quality,
            "action": action
        }

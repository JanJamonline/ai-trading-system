# signal_fusion/fusion_engine.py

class FusionEngine:
    def fuse(self, ta_signal, ta_strength, fa_signal, fa_strength):
        # Conflict → HOLD
        if ta_signal in ["BUY", "SELL"] and fa_signal not in ["BULLISH", "BEARISH"]:
            return "HOLD", "WEAK"

        if ta_signal == "BUY" and fa_signal == "BULLISH":
            return "BUY", "STRONG"

        if ta_signal == "SELL" and fa_signal == "BEARISH":
            return "SELL", "STRONG"

        if ta_signal in ["BUY", "SELL"]:
            return ta_signal, "MEDIUM"

        return "HOLD", "WEAK"

    def final_action(self, signal, quality, risk_label):
        if risk_label == "HIGH_RISK":
            return "AVOID"

        if quality == "STRONG" and signal in ["BUY", "SELL"]:
            return signal

        if quality == "MEDIUM" and signal in ["BUY", "SELL"]:
            return signal

        if quality == "WEAK":
            return "WAIT"

        return "WAIT"

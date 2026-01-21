class FusionEngine:
    def fuse(self, ta_signal, ta_strength, fa_signal, fa_strength, tf_agree):
        if not tf_agree:
            return "HOLD", "WEAK"

        if ta_signal == fa_signal:
            if ta_strength >= 70 and fa_strength >= 70:
                return ta_signal, "STRONG"
            return ta_signal, "MEDIUM"

        return "HOLD", "WEAK"

    def final_action(self, signal, quality, risk_label):
        if risk_label == "HIGH_RISK":
            return "AVOID"

        if signal == "BUY" and quality == "STRONG":
            return "BUY"

        if signal == "SELL" and quality == "STRONG":
            return "SELL"

        return "WAIT"

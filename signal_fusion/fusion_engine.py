class FusionEngine:
    def fuse(self, ta_signal, ta_strength, fa_signal, fa_strength):
        """
        Option A.3 — Confidence & Threshold Tuned Fusion
        """

        score = 0

        # TA contribution
        if ta_signal == "BUY":
            score += ta_strength
        elif ta_signal == "SELL":
            score -= ta_strength

        # FA contribution
        if fa_signal == "BULLISH":
            score += fa_strength
        elif fa_signal == "BEARISH":
            score -= fa_strength

        # Tuned thresholds
        if score >= 100:
            return "BUY", "STRONG"
        elif score <= -100:
            return "SELL", "STRONG"
        elif score >= 60:
            return "BUY", "MEDIUM"
        elif score <= -60:
            return "SELL", "MEDIUM"
        else:
            return "HOLD", "WEAK"

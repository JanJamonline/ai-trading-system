class FusionEngine:
    def fuse(self, ta_signal, ta_strength, fa_signal, fa_strength):
        """
        Combines TA + FA into a final signal and quality.
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

        # Final decision
        if score >= 80:
            return "BUY", "STRONG"
        elif score <= -80:
            return "SELL", "STRONG"
        elif score >= 40:
            return "BUY", "MEDIUM"
        elif score <= -40:
            return "SELL", "MEDIUM"
        else:
            return "HOLD", "WEAK"

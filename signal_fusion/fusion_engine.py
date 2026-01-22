class FusionEngine:
    def fuse(self, ta_signal, ta_strength, fa_signal, fa_strength):
        score = 0

        if ta_signal == "BUY":
            score += ta_strength
        elif ta_signal == "SELL":
            score -= ta_strength

        if fa_signal == "BULLISH":
            score += fa_strength
        elif fa_signal == "BEARISH":
            score -= fa_strength

        if score > 50:
            return "BUY", "STRONG", "LOW_RISK"
        elif score < -50:
            return "SELL", "STRONG", "LOW_RISK"
        else:
            return "HOLD", "WEAK", "HIGH_RISK"

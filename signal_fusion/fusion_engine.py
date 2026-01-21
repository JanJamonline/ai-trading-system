class FusionEngine:
    def combine(self, ta_signal, ta_strength, fa_signal, fa_strength):
        score = 0

        if ta_signal == "BUY":
            score += ta_strength
        elif ta_signal == "SELL":
            score -= ta_strength

        if fa_signal == "BULLISH":
            score += fa_strength
        elif fa_signal == "BEARISH":
            score -= fa_strength

        if score >= 100:
            return "BUY", "STRONG"
        elif score <= -100:
            return "SELL", "STRONG"
        elif score > 0:
            return "HOLD", "WEAK"
        else:
            return "HOLD", "WEAK"

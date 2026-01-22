class FusionEngine:
    def fuse(self, ta_signal, ta_strength, fa_signal, fa_strength):
        if ta_signal == "BUY" and fa_signal == "BULLISH":
            return "BUY", "STRONG", "LOW_RISK"
        if ta_signal == "SELL" and fa_signal == "BEARISH":
            return "SELL", "STRONG", "LOW_RISK"
        if ta_signal == "HOLD":
            return "HOLD", "WEAK", "HIGH_RISK"
        return "HOLD", "MEDIUM", "MEDIUM_RISK"

    def compute_confidence(self, ta_strength, fa_strength, quality, risk_label):
        base = (ta_strength * 0.4) + (fa_strength * 0.3)

        quality_bonus = {
            "STRONG": 20,
            "MEDIUM": 10,
            "WEAK": 0
        }.get(quality, 0)

        risk_penalty = {
            "HIGH_RISK": -30,
            "MEDIUM_RISK": -15,
            "LOW_RISK": 0
        }.get(risk_label, 0)

        score = base + quality_bonus + risk_penalty
        return max(0, min(100, int(score)))

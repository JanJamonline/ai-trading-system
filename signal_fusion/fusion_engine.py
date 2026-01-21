class FusionEngine:
    def fuse(self, ta_signal, ta_strength, fa_signal, fa_strength):
        if ta_signal == "BUY" and fa_signal == "BULLISH":
            return "BUY", "STRONG", 80
        if ta_signal == "SELL" and fa_signal == "BEARISH":
            return "SELL", "STRONG", 80

        return "NEUTRAL", "WEAK", 40

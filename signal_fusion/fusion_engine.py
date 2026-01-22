class FusionEngine:
    def derive_primary_trade_signal(self, signal, quality, risk_label):
        """
        SINGLE FINAL TRADE DECISION
        """

        if risk_label == "HIGH_RISK":
            return "HOLD"

        if signal == "BUY" and quality in ["STRONG", "MEDIUM"]:
            return "BUY"

        if signal == "SELL" and quality in ["STRONG", "MEDIUM"]:
            return "SELL"

        return "HOLD"

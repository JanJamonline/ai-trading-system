class BacktestEngine:
    def __init__(self, ta_manager, fa_manager):
        self.ta = ta_manager
        self.fa = fa_manager

    def run(self, df, symbol):
        results = []

        for i in range(len(df)):
            ta_signal, ta_strength, reason = self.ta.evaluate(i)
            fa_signal, fa_strength = self.fa.evaluate(symbol)

            final_signal = ta_signal
            quality = "WEAK"
            risk_label = "HIGH_RISK"

            results.append({
                "time": df.iloc[i]["time"],
                "symbol": symbol,
                "price": df.iloc[i]["close"],
                "ta_signal": ta_signal,
                "ta_strength": ta_strength,
                "fa_signal": fa_signal,
                "fa_strength": fa_strength,
                "signal": final_signal,
                "quality": quality,
                "risk_label": risk_label,
                "primary_trade_signal": final_signal,
                "reason": reason
            })

        return results

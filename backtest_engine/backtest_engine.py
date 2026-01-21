# backtest_engine/backtest_engine.py

class BacktestEngine:
    def __init__(self, ta, fa, fusion):
        self.ta = ta
        self.fa = fa
        self.fusion = fusion

    def run(self, df, symbol):
        results = []

        for i in range(1, len(df)):
            price = df.iloc[i]["close"]
            time = df.iloc[i]["time"]

            ta_signal, ta_strength, reason = self.ta.evaluate(i)
            fa_signal, fa_strength = self.fa.evaluate(symbol)

            signal, quality = self.fusion.fuse(
                ta_signal, ta_strength, fa_signal, fa_strength
            )

            risk_label = "HIGH_RISK" if quality == "WEAK" else "MEDIUM_RISK"
            final_action = self.fusion.final_action(signal, quality, risk_label)

            results.append({
                "time": time,
                "symbol": symbol,
                "price": price,
                "ta_signal": ta_signal,
                "ta_strength": ta_strength,
                "fa_signal": fa_signal,
                "fa_strength": fa_strength,
                "signal": signal,
                "quality": quality,
                "risk_label": risk_label,
                "final_action": final_action,
                "reason": reason
            })

        return results

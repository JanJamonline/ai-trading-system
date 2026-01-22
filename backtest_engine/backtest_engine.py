from signal_fusion.fusion_engine import FusionEngine


class BacktestEngine:
    def __init__(self, ta_5m, fa):
        self.ta_5m = ta_5m
        self.fa = fa
        self.fusion = FusionEngine()

    def run(self, df, symbol):
        results = []

        for i in range(len(df)):
            ta_signal, ta_strength, reason = self.ta_5m.evaluate(i)
            fa_signal, fa_strength = self.fa.evaluate(symbol)

            signal, quality, risk = self.fusion.fuse(
                ta_signal, ta_strength,
                fa_signal, fa_strength
            )

            final_action = self.fusion.final_action(signal, quality, risk)

            results.append({
                "time": df.iloc[i]["time"],
                "symbol": symbol,
                "price": df.iloc[i]["close"],
                "ta_signal": ta_signal,
                "ta_strength": ta_strength,
                "fa_signal": fa_signal,
                "fa_strength": fa_strength,
                "signal": signal,
                "quality": quality,
                "risk_label": risk,
                "primary_trade_signal": final_action,
                "reason": reason
            })

        return results

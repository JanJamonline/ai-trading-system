class BacktestEngine:
    def __init__(self, ta, fa, fusion):
        self.ta = ta
        self.fa = fa
        self.fusion = fusion

    def run(self, df, symbol):
        results = []

        for i in range(len(df)):
            ta_signal, ta_strength, ta_reason = self.ta.evaluate(i)
            fa_signal, fa_strength = self.fa.evaluate(symbol)

            final_signal, quality = self.fusion.fuse(
                ta_signal,
                ta_strength,
                fa_signal,
                fa_strength
            )

            results.append({
                "time": df.loc[i, "time"],
                "symbol": symbol,
                "price": df.loc[i, "close"],
                "ta_signal": ta_signal,
                "ta_strength": ta_strength,
                "ta_reason": ta_reason,
                "fa_signal": fa_signal,
                "fa_strength": fa_strength,
                "signal": final_signal,
                "quality": quality
            })

        return results

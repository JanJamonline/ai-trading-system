class BacktestEngine:
    def __init__(self, ta, fa, fusion):
        self.ta = ta
        self.fa = fa
        self.fusion = fusion

    def run(self, df, symbol):
        results = []

        for i in range(len(df)):
            ta_signal, ta_strength, reason = self.ta.evaluate(df, i)
            fa_signal, fa_strength = self.fa.evaluate(symbol)
            final_signal, combined_strength, confidence = self.fusion.fuse(
                ta_signal, ta_strength, fa_signal, fa_strength
            )

            results.append({
                "time": df.loc[i, "time"],
                "symbol": symbol,
                "ta_signal": ta_signal,
                "ta_strength": ta_strength,
                "fa_signal": fa_signal,
                "fa_strength": fa_strength,
                "combined_strength": combined_strength,
                "final_signal": final_signal,
                "confidence": confidence,
                "reason": reason
            })

        return results

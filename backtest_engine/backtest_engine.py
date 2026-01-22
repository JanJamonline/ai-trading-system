from backtest_engine.signal_evaluator import SignalEvaluator

class BacktestEngine:
    def __init__(self, ta_5m, fa, fusion):
        self.ta_5m = ta_5m
        self.fa = fa
        self.fusion = fusion
        self.evaluator = SignalEvaluator()

    def run(self, df, symbol):
        results = []

        for i in range(len(df)):
            ta_signal, ta_strength, reason = self.ta_5m.evaluate(i)
            fa_signal, fa_strength = self.fa.evaluate(symbol)

            signal, quality, risk_label = self.fusion.fuse(
                ta_signal, fa_signal
            )

            confidence_score = self.evaluator.calculate_confidence_score(
                ta_strength=ta_strength,
                fa_strength=fa_strength,
                ta_signal=ta_signal,
                fa_signal=fa_signal,
                risk_label=risk_label
            )

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
                "risk_label": risk_label,
                "primary_trade_signal": signal,
                "confidence_score": confidence_score,
                "reason": reason
            })

        return results

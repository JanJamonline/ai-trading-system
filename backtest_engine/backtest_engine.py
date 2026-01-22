# backtest_engine/backtest_engine.py

from signal_fusion.fusion_engine import FusionEngine

class BacktestEngine:
    """
    Executes signal evaluation per candle
    """

    def __init__(self, ta_5m, fa):
        self.ta_5m = ta_5m
        self.fa = fa
        self.fusion = FusionEngine()

    def run(self, df, symbol):
        results = []

        for i in range(len(df)):
            ta_signal, ta_strength, reason = self.ta_5m.evaluate(i)
            fa_signal, fa_strength = self.fa.evaluate(symbol)

            fused = self.fusion.fuse(
                ta_signal=ta_signal,
                ta_strength=ta_strength,
                fa_signal=fa_signal,
                fa_strength=fa_strength
            )

            results.append({
                "time": df.iloc[i]["time"],
                "symbol": symbol,
                "price": df.iloc[i]["close"],
                "ta_signal": ta_signal,
                "ta_strength": ta_strength,
                "fa_signal": fa_signal,
                "fa_strength": fa_strength,
                "signal": fused["signal"],
                "quality": fused["quality"],
                "risk_label": fused["risk_label"],
                "confidence": fused["confidence"],
                "confidence_bucket": fused["confidence_bucket"],
                "primary_trade_signal": fused["signal"],
                "reason": reason
            })

        return results

from signal_fusion.fusion_engine import FusionEngine

class BacktestEngine:
    def __init__(self, ta_manager, fa_manager, fusion_engine=None):
        self.ta_manager = ta_manager
        self.fa_manager = fa_manager
        self.fusion = fusion_engine or FusionEngine()

    def run(self, df, symbol):
        results = []

        for i in range(len(df)):
            ta_signal, ta_strength, reason = self.ta_manager.evaluate(i)
            fa_signal, fa_strength = self.fa_manager.evaluate(symbol)

            signal, quality, risk_label = self.fusion.fuse(
                ta_signal, ta_strength, fa_signal, fa_strength
            )

            confidence = self.fusion.compute_confidence(
                ta_strength, fa_strength, quality, risk_label
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
                "confidence_score": confidence,
                "primary_trade_signal": signal,
                "reason": reason
            })

        return results

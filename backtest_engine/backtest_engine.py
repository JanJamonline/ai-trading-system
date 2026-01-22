from signal_fusion.fusion_engine import FusionEngine


class BacktestEngine:
    def __init__(self, ta_5m, fa):
        self.ta_5m = ta_5m
        self.fa = fa
        self.fusion = FusionEngine()

    def run(self, df, symbol):
        results = []

        for i in range(len(df)):
            row = df.iloc[i]

            ta_signal, ta_strength, reason = self.ta_5m.evaluate(i)
            fa_signal, fa_strength = self.fa.evaluate(symbol)

            if ta_signal == "BUY" and fa_signal == "BULLISH":
                signal = "BUY"
                quality = "STRONG"
            elif ta_signal == "SELL" and fa_signal == "BEARISH":
                signal = "SELL"
                quality = "STRONG"
            else:
                signal = "HOLD"
                quality = "WEAK"

            risk_label = "HIGH_RISK" if quality == "WEAK" else "MEDIUM_RISK"

            primary_trade_signal = self.fusion.derive_primary_trade_signal(
                signal, quality, risk_label
            )

            results.append({
                "time": row["time"],
                "symbol": symbol,
                "price": row["close"],
                "ta_signal": ta_signal,
                "ta_strength": ta_strength,
                "fa_signal": fa_signal,
                "fa_strength": fa_strength,
                "signal": signal,
                "quality": quality,
                "risk_label": risk_label,
                "primary_trade_signal": primary_trade_signal,
                "reason": reason
            })

        return results

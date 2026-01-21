class BacktestEngine:
    def __init__(self, ta_5m, ta_15m, fa, fusion, tf_validator):
        self.ta_5m = ta_5m
        self.ta_15m = ta_15m
        self.fa = fa
        self.fusion = fusion
        self.tf_validator = tf_validator

    def run(self, df, symbol):
        results = []

        for i in range(len(df)):
            ta_signal_5m, ta_strength, risk_label, ta_reason = self.ta_5m.evaluate(i)

            # 15m confirmation (optional)
            tf_agree = True
            if self.ta_15m:
                ta_15m_signal, _, _, _ = self.ta_15m.evaluate(i)
                tf_agree = self.tf_validator.validate(ta_signal_5m, ta_15m_signal)

            fa_signal, fa_strength = self.fa.evaluate(symbol)

            final_signal, quality = self.fusion.fuse(
                ta_signal_5m,
                ta_strength,
                fa_signal,
                fa_strength,
                tf_agree
            )

            final_action = self.fusion.final_action(
                final_signal,
                quality,
                risk_label
            )

            results.append({
                "time": df.iloc[i]["time"],
                "symbol": symbol,
                "price": df.iloc[i]["close"],
                "ta_signal": ta_signal_5m,
                "ta_strength": ta_strength,
                "fa_signal": fa_signal,
                "fa_strength": fa_strength,
                "signal": final_signal,
                "quality": quality,
                "risk_label": risk_label,
                "final_action": final_action,
                "reason": ta_reason
            })

        return results

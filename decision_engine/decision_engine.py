import pandas as pd


class DecisionEngine:
    def evaluate(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()

        out["signal"] = out["ta_signal"]
        out["direction"] = out["signal"].map(
            {"BUY": "BULLISH", "SELL": "BEARISH", "HOLD": "NEUTRAL"}
        )
        out["confidence"] = out["signal"].apply(
            lambda x: 70 if x in ["BUY", "SELL"] else 0
        )
        out["reason"] = out["signal"]

        return out

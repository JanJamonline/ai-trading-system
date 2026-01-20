import pandas as pd


class TAManager:
    def compute(self, prices_df: pd.DataFrame) -> pd.DataFrame:
        df = prices_df.copy()

        df["ta_signal"] = "HOLD"
        df.loc[df["price"].diff() > 0, "ta_signal"] = "BUY"
        df.loc[df["price"].diff() < 0, "ta_signal"] = "SELL"

        return df

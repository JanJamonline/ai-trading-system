class TAManager:
    def compute(self, prices_df):
        df = prices_df.copy()
        df["trend"] = "FLAT"

        for i in range(1, len(df)):
            if df.loc[i, "close"] > df.loc[i - 1, "close"]:
                df.loc[i, "trend"] = "UP"
            elif df.loc[i, "close"] < df.loc[i - 1, "close"]:
                df.loc[i, "trend"] = "DOWN"

        return df

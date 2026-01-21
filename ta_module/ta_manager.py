class TAManager:
    def compute(self, df):
        signals = []

        for i in range(len(df)):
            if i == 0:
                signals.append("FLAT")
            else:
                if df.loc[i, "close"] > df.loc[i - 1, "close"]:
                    signals.append("UP")
                elif df.loc[i, "close"] < df.loc[i - 1, "close"]:
                    signals.append("DOWN")
                else:
                    signals.append("FLAT")

        df["ta_signal"] = signals
        return df

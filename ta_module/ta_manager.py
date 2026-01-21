class TAManager:
    def evaluate(self, df, i):
        if i == 0:
            return "HOLD", "WEAK", "NO_CONFIRMATION"

        if df.loc[i, "close"] > df.loc[i - 1, "close"]:
            return "BUY", "STRONG", "UP"
        elif df.loc[i, "close"] < df.loc[i - 1, "close"]:
            return "SELL", "STRONG", "DOWN"

        return "HOLD", "WEAK", "FLAT"

class TAManager:
    def __init__(self, df):
        self.df = df

    def evaluate(self, idx):
        if idx <= 0 or idx >= len(self.df):
            return "HOLD", 0, "HIGH_RISK", "NO_DATA"

        close = self.df.iloc[idx]["close"]
        prev_close = self.df.iloc[idx - 1]["close"]

        if close > prev_close:
            return "BUY", 70, "MEDIUM_RISK", "UP"

        if close < prev_close:
            return "SELL", 70, "MEDIUM_RISK", "DOWN"

        return "HOLD", 0, "HIGH_RISK", "NO_CONFIRMATION"

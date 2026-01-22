class TAManager:
    def __init__(self, df):
        self.df = df

    def evaluate(self, i):
        if i == 0:
            return "HOLD", 0, "NO_DATA"

        prev = self.df.iloc[i - 1]["close"]
        curr = self.df.iloc[i]["close"]

        if curr > prev:
            return "BUY", 70, "UP"
        elif curr < prev:
            return "SELL", 70, "DOWN"
        else:
            return "HOLD", 0, "FLAT"

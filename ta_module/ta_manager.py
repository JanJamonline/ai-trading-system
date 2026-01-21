class TAManager:
    def __init__(self, df):
        self.df = df.reset_index(drop=True)

    def evaluate(self, i):
        if i == 0:
            return "HOLD", 0, "NO_CONFIRMATION"

        prev = self.df.loc[i - 1, "close"]
        curr = self.df.loc[i, "close"]

        if curr > prev:
            return "BUY", 70, "UP"
        elif curr < prev:
            return "SELL", 70, "DOWN"
        else:
            return "HOLD", 0, "FLAT"

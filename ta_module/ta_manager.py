class TAManager:
    def __init__(self, df):
        self.df = df.reset_index(drop=True)

    def evaluate(self, i):
        if i == 0:
            return "HOLD", 0, "NO_CONFIRMATION"

        prev_close = self.df.loc[i - 1, "close"]
        curr_close = self.df.loc[i, "close"]

        if curr_close > prev_close:
            return "BUY", 70, "PRICE_UP"
        elif curr_close < prev_close:
            return "SELL", 70, "PRICE_DOWN"
        else:
            return "HOLD", 0, "FLAT"

class TAManager:
    """
    Technical Analysis Manager
    CONTRACT:
    evaluate(index) -> (signal, strength, reason)
    """

    def __init__(self, df):
        self.df = df

    def evaluate(self, i):
        if i == 0:
            return "HOLD", 0, "NO_DATA"

        prev = self.df.iloc[i - 1]
        curr = self.df.iloc[i]

        if curr["close"] > prev["close"]:
            return "BUY", 70, "UP"
        elif curr["close"] < prev["close"]:
            return "SELL", 70, "DOWN"
        else:
            return "HOLD", 0, "FLAT"

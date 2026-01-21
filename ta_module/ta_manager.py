class TAManager:
    """
    Technical Analysis manager for a single timeframe.
    """

    def __init__(self, df):
        self.df = df.reset_index(drop=True)

    def evaluate(self, index: int):
        """
        Simple momentum-based TA.
        """

        if index == 0:
            return "HOLD", 0, "NO_DATA"

        prev_close = self.df.loc[index - 1, "close"]
        curr_close = self.df.loc[index, "close"]

        if curr_close > prev_close:
            return "BUY", 70, "UP"
        elif curr_close < prev_close:
            return "SELL", 70, "DOWN"

        return "HOLD", 0, "FLAT"

class SignalOutcomeEvaluator:
    def __init__(self, lookahead=3):
        self.lookahead = lookahead

    def evaluate(self, signals, price_df):
        evaluated = []

        for i, s in enumerate(signals):
            future_index = i + self.lookahead

            if future_index >= len(price_df):
                s["outcome"] = "INSUFFICIENT_DATA"
                evaluated.append(s)
                continue

            entry = s["price"]
            future = price_df.loc[future_index, "close"]

            if s["signal"] == "BUY":
                s["outcome"] = "CORRECT" if future > entry else "WRONG"
            elif s["signal"] == "SELL":
                s["outcome"] = "CORRECT" if future < entry else "WRONG"
            else:
                s["outcome"] = "NEUTRAL"

            evaluated.append(s)

        return evaluated

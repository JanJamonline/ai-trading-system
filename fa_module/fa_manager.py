import pandas as pd


class FAManager:
    """
    Fundamental Analysis Manager
    CONTRACT:
    evaluate(symbol) -> (fa_signal, fa_strength)
    """

    def __init__(self, path="data/fa_data.csv"):
        try:
            self.df = pd.read_csv(path)
        except Exception:
            self.df = pd.DataFrame()

    def evaluate(self, symbol):
        if self.df.empty or "symbol" not in self.df.columns:
            return "NEUTRAL", 0

        row = self.df[self.df["symbol"] == symbol]

        if row.empty:
            return "NEUTRAL", 0

        row = row.iloc[0]

        # ✅ Flexible FA interpretation
        # Priority order: score → rating → trend
        if "score" in row:
            score = row["score"]
        elif "rating" in row:
            score = row["rating"]
        elif "trend" in row:
            score = 70 if row["trend"] == "POSITIVE" else 30
        else:
            return "NEUTRAL", 0

        if score >= 70:
            return "BULLISH", 70
        elif score <= 30:
            return "BEARISH", 70
        else:
            return "NEUTRAL", 0

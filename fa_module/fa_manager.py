import pandas as pd
from fa_module.fa_rules import evaluate_fa

class FAManager:
    def __init__(self, path="data/fa_data.csv"):
        self.df = pd.read_csv(path)

    def evaluate(self, symbol):
        row = self.df[self.df["symbol"] == symbol]

        if row.empty:
            return "NEUTRAL", "WEAK"

        return evaluate_fa(row.iloc[0])

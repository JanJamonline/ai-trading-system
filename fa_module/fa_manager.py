import pandas as pd
from fa_module.fa_rules import evaluate_fa


class FAManager:
    def __init__(self, fa_csv_path: str):
        self.df = pd.read_csv(fa_csv_path)

    def evaluate(self, symbol):
        row = self.df[self.df["symbol"] == symbol]

        if row.empty:
            return "NEUTRAL", 0

        return evaluate_fa(row.iloc[0])

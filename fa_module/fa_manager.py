from fa_module.fa_rules import evaluate_fa

class FAManager:
    def __init__(self, df):
        self.df = df

    def evaluate(self, symbol):
        row = self.df[self.df["symbol"] == symbol]

        if row.empty:
            return "NEUTRAL", 0

        return evaluate_fa(row.iloc[0])

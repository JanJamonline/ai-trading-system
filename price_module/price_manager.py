import pandas as pd


class PriceManager:
    def __init__(self, csv_path: str, symbol: str):
        self.csv_path = csv_path
        self.symbol = symbol
        self.df = self._load_prices()

    def _load_prices(self):
        df = pd.read_csv(self.csv_path)

        required = {"time", "symbol", "price"}
        if not required.issubset(df.columns):
            raise ValueError("CSV must contain time, symbol, price columns")

        df = df[df["symbol"] == self.symbol].copy()
        df["time"] = pd.to_datetime(df["time"])
        df.reset_index(drop=True, inplace=True)

        return df

    def get_prices(self) -> pd.DataFrame:
        return self.df

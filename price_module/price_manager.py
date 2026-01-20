import pandas as pd

class PriceManager:
    def __init__(self, csv_path, symbol):
        self.symbol = symbol

        df = pd.read_csv(csv_path)

        # Normalize column names
        df.columns = [c.lower().strip() for c in df.columns]

        # Enforce required schema
        if "price" in df.columns and "close" not in df.columns:
            df["close"] = df["price"]

        required = {"time", "symbol", "close"}
        missing = required - set(df.columns)

        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        df["time"] = df["time"].astype(str)

        self.df = df[df["symbol"] == symbol].reset_index(drop=True)

    def get_prices(self):
        return self.df

import pandas as pd

class PriceManager:
    def __init__(self, csv_path: str, symbol: str):
        self.csv_path = csv_path
        self.symbol = symbol

    def load_prices(self) -> pd.DataFrame:
        df = pd.read_csv(self.csv_path)

        df.columns = [c.lower() for c in df.columns]

        if "close" not in df.columns:
            raise ValueError("CSV must contain a 'close' column")

        return df.reset_index(drop=True)

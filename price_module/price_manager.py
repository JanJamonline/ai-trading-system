import pandas as pd

class PriceManager:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df["time"] = pd.to_datetime(self.df["time"])

    def get_prices(self):
        return self.df

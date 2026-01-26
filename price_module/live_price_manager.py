import yfinance as yf
import pandas as pd
from pathlib import Path
import os


class LivePriceManager:
    def __init__(self, symbol):
        self.symbol = symbol.upper()
        self.yahoo_symbol = symbol + ".NS"

    def fetch(self, interval="5m"):
        try:
            df = yf.download(
                self.yahoo_symbol,
                period="1d",
                interval=interval,
                progress=False
            )

            if df.empty:
                raise ValueError("Empty live data")

            # Handle datetime index
            if isinstance(df.index, pd.DatetimeIndex):
                df = df.reset_index()

            # Flatten column names
            df.columns = [
                c[0].lower() if isinstance(c, tuple) else str(c).lower()
                for c in df.columns
            ]

            if "datetime" in df.columns:
                df.rename(columns={"datetime": "time"}, inplace=True)
            if "date" in df.columns:
                df.rename(columns={"date": "time"}, inplace=True)

            required = {"time", "open", "high", "low", "close", "volume"}
            if not required.issubset(df.columns):
                raise ValueError("Live schema mismatch")

            return df[list(required)].sort_values("time")

        except Exception as e:
            print(f"⚠️ LIVE DATA FAILED ({e}) — FALLING BACK TO CSV")
            return self._fallback_csv(interval)

    def _fallback_csv(self, interval):
        csv_path = Path("data") / f"{self.symbol}_{interval}.csv"

        # CSV does not exist
        if not csv_path.exists():
            print(f"⚠️ CSV NOT FOUND: {csv_path}")
            return pd.DataFrame()

        # CSV exists but is empty
        if os.path.getsize(csv_path) == 0:
            print(f"⚠️ CSV EMPTY: {csv_path}")
            return pd.DataFrame()

        try:
            df = pd.read_csv(csv_path)
        except Exception as e:
            print(f"⚠️ CSV READ FAILED ({e})")
            return pd.DataFrame()

        df.columns = [c.lower() for c in df.columns]

        if "time" not in df.columns:
            print("⚠️ CSV missing time column")
            return pd.DataFrame()

        return df
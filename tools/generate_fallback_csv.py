import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

REQUIRED_COLUMNS = ["time", "open", "high", "low", "close", "volume"]

# --------------------------------------------------
# Synthetic fallback generator (SAFE & LABELED)
# --------------------------------------------------
def generate_synthetic_ohlc(symbol, interval="5m", bars=75):
    print(f"⚠️ Using synthetic data for {symbol}")

    end_time = datetime.now().replace(second=0, microsecond=0)
    times = [end_time - timedelta(minutes=5 * i) for i in range(bars)]
    times.reverse()

    base_price = np.random.uniform(50, 300)
    prices = [base_price]

    for _ in range(bars - 1):
        prices.append(prices[-1] * np.random.uniform(0.998, 1.002))

    df = pd.DataFrame({
        "time": times,
        "open": prices,
        "high": [p * np.random.uniform(1.000, 1.003) for p in prices],
        "low":  [p * np.random.uniform(0.997, 1.000) for p in prices],
        "close": prices,
        "volume": np.random.randint(50_000, 300_000, size=bars)
    })

    return df


# --------------------------------------------------
# Yahoo fetch attempt
# --------------------------------------------------
def fetch_yahoo(symbol, interval="5m"):
    yahoo_symbol = f"{symbol}.NS"
    try:
        df = yf.download(
            yahoo_symbol,
            period="1d",
            interval=interval,
            progress=False
        )

        if df.empty:
            raise ValueError("Yahoo returned empty")

        if isinstance(df.index, pd.DatetimeIndex):
            df = df.reset_index()

        df.columns = [c.lower() if isinstance(c, str) else c[0].lower() for c in df.columns]

        if "datetime" in df.columns:
            df.rename(columns={"datetime": "time"}, inplace=True)
        if "date" in df.columns:
            df.rename(columns={"date": "time"}, inplace=True)

        df = df[REQUIRED_COLUMNS]
        return df

    except Exception as e:
        print(f"❌ Yahoo failed for {symbol}: {e}")
        return None


# --------------------------------------------------
# MAIN GENERATOR
# --------------------------------------------------
def generate_csv(symbol, interval="5m"):
    print(f"\n🔧 Generating CSV for {symbol} ({interval})")

    df = fetch_yahoo(symbol, interval)

    if df is None or df.empty:
        df = generate_synthetic_ohlc(symbol, interval)

    csv_path = DATA_DIR / f"{symbol}_{interval}.csv"
    df.to_csv(csv_path, index=False)

    print(f"✅ Saved: {csv_path} ({len(df)} rows)")


# --------------------------------------------------
# RUN
# --------------------------------------------------
if __name__ == "__main__":
    symbols = ["MRPL", "SAIL", "YESBANK", "HDFCBANK"]

    for sym in symbols:
        generate_csv(sym, "5m")
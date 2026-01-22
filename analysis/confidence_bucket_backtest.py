# analysis/confidence_bucket_backtest.py

import os
import sys
import pandas as pd

# ✅ Ensure project root is on PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from multi_symbol_engine import generate_signals_multi


def evaluate_confidence_buckets(symbols):
    print("\n📊 RUNNING CONFIDENCE BUCKET BACKTEST\n")

    results = generate_signals_multi(symbols)
    df = pd.DataFrame(results)

    if df.empty:
        print("⚠️ No data available")
        return

    required_cols = {
        "primary_trade_signal",
        "confidence_bucket",
        "price"
    }

    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # --- Determine outcome ---
    df["next_price"] = df["price"].shift(-1)

    df["outcome"] = "NEUTRAL"

    df.loc[
        (df["primary_trade_signal"] == "BUY") &
        (df["next_price"] > df["price"]),
        "outcome"
    ] = "WIN"

    df.loc[
        (df["primary_trade_signal"] == "BUY") &
        (df["next_price"] <= df["price"]),
        "outcome"
    ] = "LOSS"

    df.loc[
        (df["primary_trade_signal"] == "SELL") &
        (df["next_price"] < df["price"]),
        "outcome"
    ] = "WIN"

    df.loc[
        (df["primary_trade_signal"] == "SELL") &
        (df["next_price"] >= df["price"]),
        "outcome"
    ] = "LOSS"

    actionable = df[df["primary_trade_signal"].isin(["BUY", "SELL"])]

    report = []

    for bucket in sorted(actionable["confidence_bucket"].unique()):
        subset = actionable[actionable["confidence_bucket"] == bucket]

        total = len(subset)
        wins = len(subset[subset["outcome"] == "WIN"])
        losses = len(subset[subset["outcome"] == "LOSS"])
        win_rate = round((wins / total) * 100, 2) if total else 0

        report.append({
            "confidence_bucket": bucket,
            "trades": total,
            "wins": wins,
            "losses": losses,
            "win_rate_%": win_rate
        })

    report_df = pd.DataFrame(report)

    print("\n========== CONFIDENCE BUCKET PERFORMANCE ==========\n")
    print(report_df.to_string(index=False))
    print("\n===================================================\n")


if __name__ == "__main__":
    symbols = ["TATASTEEL"]
    evaluate_confidence_buckets(symbols)

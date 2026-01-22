import os
import sys
import streamlit as st
import pandas as pd

# =====================================================
# FIX IMPORT PATH (CRITICAL & SAFE)
# =====================================================
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from multi_symbol_engine import generate_signals_multi

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="AI Trading System — PRIMARY SIGNAL VIEW",
    layout="wide"
)

st.title("AI Trading System — PRIMARY SIGNAL VIEW")
st.caption("Read-only decision intelligence • No auto trading")

# =====================================================
# INPUT
# =====================================================
symbols_input = st.text_input(
    "Enter symbols (comma separated)",
    value="TATASTEEL"
)

generate = st.button("Generate Signals")

# =====================================================
# HELPERS
# =====================================================
DATA_DIR = "data"

def validate_symbols(symbols):
    valid, invalid = [], []
    for sym in symbols:
        csv_path = os.path.join(DATA_DIR, f"{sym}_5m.csv")
        if os.path.exists(csv_path):
            valid.append(sym)
        else:
            invalid.append(sym)
    return valid, invalid


def color_signal(val):
    if val == "BUY":
        return "background-color:#d4f7d4;font-weight:bold"
    if val == "SELL":
        return "background-color:#ffd6d6;font-weight:bold"
    if val == "HOLD":
        return "background-color:#f0f0f0;font-weight:bold"
    return ""

# =====================================================
# MAIN
# =====================================================
if generate:

    raw_symbols = [s.strip().upper() for s in symbols_input.split(",") if s.strip()]

    if not raw_symbols:
        st.error("Please enter at least one symbol.")
        st.stop()

    valid_symbols, invalid_symbols = validate_symbols(raw_symbols)

    if invalid_symbols:
        st.warning(
            f"No data available for: {', '.join(invalid_symbols)}. "
            "These symbols were skipped."
        )

    if not valid_symbols:
        st.error("No valid symbols found.")
        st.stop()

    # -------------------------
    # ENGINE CALL (UNCHANGED)
    # -------------------------
    results = generate_signals_multi(valid_symbols)

    if isinstance(results, list):
        df = pd.DataFrame(results)
    else:
        df = results.copy()

    if df.empty:
        st.warning("No results returned.")
        st.stop()

    if {"symbol", "time"}.issubset(df.columns):
        df = df.sort_values(["symbol", "time"]).reset_index(drop=True)

    # =====================================================
    # PER SYMBOL PRIMARY DECISION
    # =====================================================
    st.markdown("---")
    st.subheader("🎯 PRIMARY TRADE DECISION (Per Symbol)")

    for symbol in valid_symbols:
        sym_df = df[df["symbol"] == symbol]
        if sym_df.empty:
            continue

        latest = sym_df.iloc[-1]

        st.markdown(f"### {symbol}")
        c1, c2, c3, c4 = st.columns(4)

        c1.metric("PRIMARY SIGNAL", latest.get("primary_trade_signal", "NA"))
        c2.metric("CONFIDENCE", f"{latest.get('confidence', 0)}%")
        c3.metric("CONFIDENCE BUCKET", latest.get("confidence_bucket", "NA"))
        c4.metric("RISK", latest.get("risk_label", "NA"))

        st.markdown("---")

    # =====================================================
    # TABLE
    # =====================================================
    st.subheader("Signal Breakdown (Review Only)")
    styled_df = df.style.applymap(color_signal, subset=["primary_trade_signal"])
    st.dataframe(styled_df, use_container_width=True)

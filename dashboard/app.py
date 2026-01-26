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
    value="TATASTEEL,MRPL,SAIL,YESBANK,HDFCBANK"
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
    if val == "NO_DATA":
        return "background-color:#f7f7f7;font-style:italic;color:#777"
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
            f"No CSV data found for: {', '.join(invalid_symbols)}. "
            "These symbols will be shown as NO DATA."
        )

    if not valid_symbols:
        st.error("No valid symbols found.")
        st.stop()

    # -------------------------
    # ENGINE CALL (SAFE)
    # -------------------------
    try:
        results = generate_signals_multi(valid_symbols)
    except Exception as e:
        st.error(f"Signal engine failed: {e}")
        st.stop()

    # Normalize results to DataFrame
    if results is None:
        results_df = pd.DataFrame()
    elif isinstance(results, list):
        results_df = pd.DataFrame(results)
    else:
        results_df = results.copy()

    # =====================================================
    # PER SYMBOL PRIMARY DECISION (OPTION B)
    # =====================================================
    st.markdown("---")
    st.subheader("🎯 PRIMARY TRADE DECISION (Per Symbol)")

    summary_rows = []

    for symbol in raw_symbols:
        sym_df = (
            results_df[results_df["symbol"] == symbol]
            if not results_df.empty and "symbol" in results_df.columns
            else pd.DataFrame()
        )

        if sym_df.empty:
            summary_rows.append({
                "symbol": symbol,
                "primary_trade_signal": "NO_DATA",
                "confidence": None,
                "confidence_bucket": "NO_DATA",
                "risk_label": "NO_DATA",
                "status": "NO DATA AVAILABLE"
            })
        else:
            latest = sym_df.sort_values("time").iloc[-1]
            summary_rows.append({
                "symbol": symbol,
                "primary_trade_signal": latest.get("primary_trade_signal", "NA"),
                "confidence": latest.get("confidence", 0),
                "confidence_bucket": latest.get("confidence_bucket", "NA"),
                "risk_label": latest.get("risk_label", "NA"),
                "status": "OK"
            })

    summary_df = pd.DataFrame(summary_rows)

    for _, row in summary_df.iterrows():
        st.markdown(f"### {row['symbol']}")
        c1, c2, c3, c4 = st.columns(4)

        c1.metric("PRIMARY SIGNAL", row["primary_trade_signal"])
        c2.metric(
            "CONFIDENCE",
            "-" if row["confidence"] is None else f"{row['confidence']}%"
        )
        c3.metric("CONFIDENCE BUCKET", row["confidence_bucket"])
        c4.metric("RISK", row["risk_label"])

        if row["primary_trade_signal"] == "NO_DATA":
            st.info("No usable live or fallback data for this symbol yet.")

        st.markdown("---")

    # =====================================================
    # TABLE (ONLY IF DATA EXISTS)
    # =====================================================
    st.subheader("Signal Breakdown (Review Only)")

    if results_df.empty:
        st.warning("No signal rows generated for any symbol.")
        st.stop()

    styled_df = results_df.style.applymap(
        color_signal,
        subset=["primary_trade_signal"]
    )
    st.dataframe(styled_df, use_container_width=True)
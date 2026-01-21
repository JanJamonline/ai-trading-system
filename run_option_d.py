import pandas as pd

from multi_symbol_engine import generate_signals_multi
from analysis.per_symbol.signal_outcome import SignalOutcomeEvaluator
from analysis.per_symbol.signal_accuracy import SignalAccuracy
from analysis.per_symbol.flip_analysis import FlipAnalysis

def run_option_d(symbol):
    print(f"\nOPTION D — Per Symbol Analysis: {symbol}\n")

    signals = generate_signals_multi([symbol])

    price_df = pd.read_csv(f"data/{symbol}_5m.csv")
    price_df.columns = [c.lower() for c in price_df.columns]

    outcome = SignalOutcomeEvaluator(lookahead=3)
    evaluated = outcome.evaluate(signals, price_df)

    accuracy = SignalAccuracy().compute(evaluated)
    flips = FlipAnalysis().analyze(evaluated)

    print("Signal Accuracy:")
    for k, v in accuracy.items():
        print(f"{k}: {v}")

    print("\nFlip Analysis:")
    print(flips)

if __name__ == "__main__":
    run_option_d("TATASTEEL")

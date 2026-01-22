import sys
import os

# ✅ ENSURE PROJECT ROOT IS ON PATH
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from multi_symbol_engine import generate_signals_multi

def main():
    print("AI Trading System starting...")
    symbols = ["TATASTEEL"]
    results = generate_signals_multi(symbols)
    print(f"Generated {len(results)} signals")

if __name__ == "__main__":
    main()

import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from multi_symbol_engine import generate_signals_multi
from backtest_engine.signal_evaluator import SignalEvaluator


def run_primary_backtest():
    print("\n🔍 RUNNING PRIMARY SIGNAL BACKTEST\n")

    symbols = ["TATASTEEL"]
    results = generate_signals_multi(symbols)

    evaluator = SignalEvaluator()
    report = evaluator.evaluate_primary_signal(results)

    print("========== PRIMARY SIGNAL PERFORMANCE ==========")
    for k, v in report.items():
        print(f"{k.upper():15}: {v}")
    print("===============================================\n")


if __name__ == "__main__":
    run_primary_backtest()

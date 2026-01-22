from multi_symbol_engine import generate_signals_multi
from analysis.primary_signal_backtest import run_primary_signal_backtest


if __name__ == "__main__":
    symbols = ["TATASTEEL"]

    print("\n🔍 Running PRIMARY SIGNAL BACKTEST...\n")

    results = generate_signals_multi(symbols)
    report = run_primary_signal_backtest(results)

    print("========== PRIMARY SIGNAL BACKTEST REPORT ==========")
    print(f"Total Trades: {report['total_trades']}")
    print(f"Win Rate: {report['win_rate']}%")
    print(f"Total PnL: {report['total_pnl']}")
    print(f"Average PnL per Trade: {report['avg_pnl']}")
    print("===================================================")

    if report["total_trades"] > 0:
        print("\nTrade Details:")
        print(report["trades"])

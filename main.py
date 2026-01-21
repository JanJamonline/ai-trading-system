from multi_symbol_engine import generate_signals_multi

def main():
    print("AI Trading System V1 starting...")

    symbols = ["TATASTEEL"]
    results = generate_signals_multi(symbols)

    for r in results:
        print(r)

if __name__ == "__main__":
    main()

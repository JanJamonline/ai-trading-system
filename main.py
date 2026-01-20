from multi_symbol_engine import generate_signals_multi


def main():
    print("AI Trading System V1 starting...")
    symbols = ["TATASTEEL"]

    df = generate_signals_multi(symbols)
    print(df.tail())


if __name__ == "__main__":
    main()

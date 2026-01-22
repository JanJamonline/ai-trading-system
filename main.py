from multi_symbol_engine import generate_signals_multi

def main():
    print("AI Trading System starting...")
    symbols = ["TATASTEEL"]
    df = generate_signals_multi(symbols)
    print(df[-5:])

if __name__ == "__main__":
    main()

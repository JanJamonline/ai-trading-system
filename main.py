from multi_symbol_engine import generate_signals

def main():
    results = generate_signals()

    for r in results:
        print(r)

if __name__ == "__main__":
    main()

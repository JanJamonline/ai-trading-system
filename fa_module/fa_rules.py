def evaluate_fa(row):
    """
    Expected columns in fa_data.csv:
    symbol, score
    """

    score = row.get("score", 0)

    if score >= 70:
        return "BULLISH", 70
    elif score <= 30:
        return "BEARISH", 70
    else:
        return "NEUTRAL", 0

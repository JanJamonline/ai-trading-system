def evaluate_fa(row):
    """
    Normalize FA score into signal + strength (0–100)
    """
    if row is None or "score" not in row:
        return "NEUTRAL", 0

    score = row["score"]

    if score >= 75:
        return "BULLISH", 80
    elif score >= 60:
        return "BULLISH", 60
    elif score >= 45:
        return "NEUTRAL", 40
    elif score >= 30:
        return "BEARISH", 60
    else:
        return "BEARISH", 80

def evaluate_fa(row):
    score = float(row.get("fa_score", 0))

    if score >= 70:
        return "BULLISH", 70
    elif score <= 30:
        return "BEARISH", 70
    else:
        return "NEUTRAL", 40

def evaluate_fa(row):
    revenue = row["revenue_growth"]
    profit = row["profit_growth"]
    debt = row["debt_to_equity"]

    score = 0

    if revenue > 10:
        score += 30
    if profit > 5:
        score += 30
    if debt < 1:
        score += 20

    if score >= 60:
        return "BULLISH", "STRONG"
    elif score >= 40:
        return "BULLISH", "MEDIUM"
    elif score >= 20:
        return "NEUTRAL", "WEAK"

    return "BEARISH", "STRONG"

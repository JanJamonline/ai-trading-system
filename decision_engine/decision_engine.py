class DecisionEngine:
    """
    Orchestrates higher-level trade decision logic.
    Currently passive (read-only system).
    """

    def assess(self, row):
        return row["primary_trade_signal"]

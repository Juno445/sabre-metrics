"""Weighted Ticket Complexity Score utilities."""


def calculate_wtcs(
    low: int,
    medium: int,
    high: int,
    urgent: int,
    stddev: float,
) -> float:
    """Calculate Weighted Ticket Complexity Score (WTCS)."""
    counts = [low, medium, high, urgent]
    if any(c < 0 for c in counts):
        raise ValueError("Ticket counts must be non-negative")
    if stddev < 0:
        raise ValueError("stddev must be non-negative")

    weighted_total = (
        low * 0.1
        + medium * 0.2
        + high * 0.3
        + urgent * 0.4
    )
    return weighted_total * stddev

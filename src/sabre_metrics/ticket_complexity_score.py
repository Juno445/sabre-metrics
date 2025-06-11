"""Ticket Complexity Score calculation utilities."""
from typing import Sequence


def calculate_tcs(low: int, medium: int, high: int, urgent: int) -> float:
    """Calculate the Ticket Complexity Score (TCS).

    The score weights ticket counts by priority and scales the result by 2.
    Negative ticket counts are not allowed.
    """
    counts = [low, medium, high, urgent]
    if any(c < 0 for c in counts):
        raise ValueError("Ticket counts must be non-negative")

    score = (
        (low * 0.1)
        + (medium * 0.2)
        + (high * 0.3)
        + (urgent * 0.4)
    )
    return score * 2

"""Weighted Real Technician Value utilities."""


def calculate_wrtv(
    agent_time_score: float,
    low: int,
    medium: int,
    high: int,
    urgent: int,
) -> float:
    """Calculate Weighted Real Technician Value (WRTV)."""
    counts = [low, medium, high, urgent]
    if any(c < 0 for c in counts):
        raise ValueError("Ticket counts must be non-negative")

    weighted_total = (
        low * 0.1
        + medium * 0.2
        + high * 0.3
        + urgent * 0.4
    )
    return (agent_time_score * weighted_total) * 0.1058

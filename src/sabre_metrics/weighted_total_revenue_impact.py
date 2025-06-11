"""Weighted Total Revenue Impact utilities."""

from __future__ import annotations


def calculate_wtri(
    medium_loss: float,
    high_loss: float,
    urgent_loss: float,
    violations: int,
    *,
    weight_medium: float = 1.0,
    weight_high: float = 1.0,
    weight_urgent: float = 1.0,
) -> float:
    """Calculate Weighted Total Revenue Impact (WTRI).

    Each loss component can be scaled with a custom weight before averaging
    by the number of SLA-violating tickets.
    """
    if violations <= 0:
        raise ValueError("violations must be greater than zero")

    losses = [medium_loss, high_loss, urgent_loss]
    weights = [weight_medium, weight_high, weight_urgent]
    if any(v < 0 for v in losses + weights):
        raise ValueError("Loss amounts and weights must be non-negative")

    weighted_total = (
        medium_loss * weight_medium
        + high_loss * weight_high
        + urgent_loss * weight_urgent
    )
    return weighted_total / violations

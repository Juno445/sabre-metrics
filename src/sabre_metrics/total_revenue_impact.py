"""Total Revenue Impact utilities."""


def calculate_tri(
    medium_loss: float,
    high_loss: float,
    urgent_loss: float,
    violations: int,
) -> float:
    """Calculate average revenue at risk per SLA-violating ticket."""
    if violations <= 0:
        raise ValueError("violations must be greater than zero")
    return (medium_loss + high_loss + urgent_loss) / violations

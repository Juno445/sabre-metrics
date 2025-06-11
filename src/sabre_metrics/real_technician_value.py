"""Real Technician Value calculation utilities."""


def calculate_rtv(agent_time_score: float, ticket_complexity_score: float) -> float:
    """Calculate Real Technician Value (RTV).

    RTV blends time efficiency with complexity handled.
    Negative inputs are allowed but may not be meaningful.
    """
    return (agent_time_score * (ticket_complexity_score * 2)) / 100

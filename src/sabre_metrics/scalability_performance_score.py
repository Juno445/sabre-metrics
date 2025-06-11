"""Scalability Performance Score utilities."""


def calculate_sps(
    agent_tickets: float,
    team_avg_tickets: float,
    agent_resolution_time: float,
    team_avg_resolution_time: float,
) -> float:
    """Calculate Comparative Scalability Performance Score (SPS).

    Formula:
        (
            agent_tickets / team_avg_tickets
        ) * (
            team_avg_resolution_time / agent_resolution_time
        )
    """
    if team_avg_tickets == 0 or agent_resolution_time == 0:
        raise ValueError("Inputs would lead to division by zero")

    return (
        agent_tickets / team_avg_tickets
    ) * (
        team_avg_resolution_time / agent_resolution_time
    )

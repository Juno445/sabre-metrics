"""Weighted Scalability Performance Score utilities."""

from __future__ import annotations


def calculate_wsps(
    agent_tickets: float,
    team_avg_tickets: float,
    agent_resolution_time: float,
    team_avg_resolution_time: float,
) -> float:
    """Calculate Weighted Scalability Performance Score (WSPS)."""
    if team_avg_tickets <= 0 or agent_resolution_time <= 0:
        raise ValueError("Inputs would lead to division by zero")

    return (
        (agent_tickets / team_avg_tickets) ** 0.7
        * (team_avg_resolution_time / agent_resolution_time) ** 1.3
    )

"""Weighted User Friction Score utilities."""

from __future__ import annotations


def calculate_wufs(
    reply_count: int,
    reassign_count: int,
    time_ms: float,
    ticket_count: int,
) -> float:
    """Calculate time-weighted User Friction Score in minutes per ticket."""
    if ticket_count <= 0:
        raise ValueError("ticket_count must be greater than zero")

    total_minutes = reply_count * 2 + reassign_count * 5 + time_ms / 60000
    return total_minutes / ticket_count

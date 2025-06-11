"""Weighted Agent Time Score utilities."""

from __future__ import annotations
from typing import Sequence


def calculate_wats(
    resolution_times: Sequence[float],
    response_times: Sequence[float],
    first_response_times: Sequence[float],
    *,
    res_weight: float = 1.0,
    resp_weight: float = 1.0,
    first_weight: float = 1.0,
) -> float:
    """Calculate the Weighted Agent Time Score (WATS)."""

    if not (
        resolution_times
        and response_times
        and first_response_times
    ):
        raise ValueError("All time sequences must be non-empty")

    if any(w < 0 for w in (res_weight, resp_weight, first_weight)):
        raise ValueError("Weights must be non-negative")

    avg_res = sum(resolution_times) / len(resolution_times)
    avg_resp = sum(response_times) / len(response_times)
    avg_first = sum(first_response_times) / len(first_response_times)

    denominator = (
        (avg_res**res_weight) * 0.5
        + (avg_resp**resp_weight) * 0.2
        + (avg_first**first_weight) * 0.3
    )
    if denominator == 0:
        raise ValueError("Denominator is zero; check input values")

    return 100 / denominator

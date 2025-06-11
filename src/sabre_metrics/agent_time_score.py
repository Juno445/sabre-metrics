"""Utilities for calculating support metrics."""

from typing import Sequence


def calculate_ats(
    resolution_times: Sequence[float],
    response_times: Sequence[float],
    first_response_times: Sequence[float],
) -> float:
    """Calculate the Agent Time Score (ATS).

    The formula mirrors the SQL example from the documentation:
    ``ATS = 100 / ((avg(resolution) * 0.5)
                   + (avg(response) * 0.2)
                   + (avg(first_response) * 0.3))``
    """
    if not (resolution_times and response_times and first_response_times):
        raise ValueError("All time sequences must be non-empty")

    avg_res = sum(resolution_times) / len(resolution_times)
    avg_resp = sum(response_times) / len(response_times)
    avg_first_resp = sum(first_response_times) / len(first_response_times)

    denominator = (avg_res * 0.5) + (avg_resp * 0.2) + (avg_first_resp * 0.3)
    if denominator == 0:
        raise ValueError("Denominator is zero; check input values")

    return 100 / denominator

import pytest
from sabre_metrics.ticket_complexity_score import calculate_tcs


def test_calculate_tcs_basic():
    score = calculate_tcs(10, 5, 2, 1)
    expected = ((10 * 0.1) + (5 * 0.2) + (2 * 0.3) + (1 * 0.4)) * 2
    assert score == pytest.approx(expected)


def test_tcs_negative():
    with pytest.raises(ValueError):
        calculate_tcs(-1, 0, 0, 0)

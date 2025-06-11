import pytest
from sabre_metrics.weighted_ticket_complexity_score import calculate_wtcs


def test_calculate_wtcs_basic():
    score = calculate_wtcs(20, 10, 1, 0, 1.788)
    expected = ((20 * 0.1) + (10 * 0.2) + (1 * 0.3) + (0 * 0.4)) * 1.788
    assert score == pytest.approx(expected)


def test_wtcs_negative():
    with pytest.raises(ValueError):
        calculate_wtcs(1, -1, 0, 0, 1.0)
    with pytest.raises(ValueError):
        calculate_wtcs(1, 1, 0, 0, -0.5)

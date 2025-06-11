import pytest
from sabre_metrics.scalability_performance_score import calculate_sps


def test_calculate_sps_basic():
    score = calculate_sps(50, 40, 2.0, 3.0)
    expected = (50 / 40) * (3.0 / 2.0)
    assert score == pytest.approx(expected)


def test_sps_zero_division():
    with pytest.raises(ValueError):
        calculate_sps(10, 0, 1, 1)
    with pytest.raises(ValueError):
        calculate_sps(10, 5, 0, 1)

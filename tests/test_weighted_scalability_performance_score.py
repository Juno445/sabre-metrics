import pytest
from sabre_metrics.weighted_scalability_performance_score import calculate_wsps


def test_calculate_wsps_basic():
    score = calculate_wsps(50, 40, 2.0, 3.0)
    expected = (50 / 40) ** 0.7 * (3.0 / 2.0) ** 1.3
    assert score == pytest.approx(expected)


def test_wsps_zero_division():
    with pytest.raises(ValueError):
        calculate_wsps(10, 0, 1, 1)
    with pytest.raises(ValueError):
        calculate_wsps(10, 5, 0, 1)

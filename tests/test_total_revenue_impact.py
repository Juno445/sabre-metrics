import pytest
from sabre_metrics.total_revenue_impact import calculate_tri


def test_calculate_tri_basic():
    score = calculate_tri(8000, 40000, 75000, 180)
    expected = (8000 + 40000 + 75000) / 180
    assert score == pytest.approx(expected)


def test_tri_zero_violations():
    with pytest.raises(ValueError):
        calculate_tri(1, 1, 1, 0)

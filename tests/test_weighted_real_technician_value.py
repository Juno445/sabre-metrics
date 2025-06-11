import pytest
import pytest
from sabre_metrics.weighted_real_technician_value import calculate_wrtv


def test_calculate_wrtv_basic():
    score = calculate_wrtv(95, 20, 10, 5, 2)
    weighted_total = (20 * 0.1) + (10 * 0.2) + (5 * 0.3) + (2 * 0.4)
    expected = (95 * weighted_total) * 0.1058
    assert score == pytest.approx(expected)


def test_wrtv_negative():
    with pytest.raises(ValueError):
        calculate_wrtv(10, -1, 0, 0, 0)

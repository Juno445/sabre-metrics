import pytest
from sabre_metrics.real_technician_value import calculate_rtv


def test_calculate_rtv():
    ats = 80
    tcs = 10
    expected = (ats * (tcs * 2)) / 100
    assert calculate_rtv(ats, tcs) == pytest.approx(expected)

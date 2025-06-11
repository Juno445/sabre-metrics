import pytest
from sabre_metrics.weighted_user_friction_score import calculate_wufs


def test_calculate_wufs_basic():
    score = calculate_wufs(4, 1, 120000, 5)
    expected = (4 * 2 + 1 * 5 + 120000 / 60000) / 5
    assert score == pytest.approx(expected)


def test_wufs_zero_tickets():
    with pytest.raises(ValueError):
        calculate_wufs(1, 1, 1000, 0)

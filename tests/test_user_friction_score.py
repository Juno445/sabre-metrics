import pytest
from sabre_metrics.user_friction_score import calculate_ufs


def test_calculate_ufs_basic():
    score = calculate_ufs(4, 1, 120000, 5)
    expected = (4 * 2 + 1 * 5 + 120000 / 60000) / 5
    assert score == pytest.approx(expected)


def test_ufs_zero_tickets():
    with pytest.raises(ValueError):
        calculate_ufs(1, 1, 1000, 0)

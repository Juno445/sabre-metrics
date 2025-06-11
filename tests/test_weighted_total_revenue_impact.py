from sabre_metrics.weighted_total_revenue_impact import calculate_wtri


def test_wtri_basic():
    assert calculate_wtri(100, 200, 300, 2) == 300.0


def test_wtri_weights():
    result = calculate_wtri(
        100,
        200,
        300,
        2,
        weight_medium=0.5,
        weight_high=1.0,
        weight_urgent=1.5,
    )
    assert result == (100 * 0.5 + 200 * 1.0 + 300 * 1.5) / 2

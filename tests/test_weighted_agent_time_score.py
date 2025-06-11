from sabre_metrics.agent_time_score import calculate_ats
from sabre_metrics.weighted_agent_time_score import calculate_wats


def test_wats_matches_ats():
    res = [10, 12, 8]
    resp = [2, 1, 3]
    first = [1, 2, 1]
    assert calculate_wats(res, resp, first) == calculate_ats(res, resp, first)


def test_wats_custom_weights():
    value = calculate_wats([10], [2], [1], res_weight=1.2, resp_weight=0.8)
    assert round(value, 2) == round(100 / ((10**1.2) * 0.5 + (2**0.8) * 0.2 + (1**1.0) * 0.3), 2)

import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
import pytest
from sabre_metrics.agent_time_score import calculate_ats


def test_calculate_ats_basic():
    res_times = [10, 12, 8]
    resp_times = [2, 1, 3]
    first_resp_times = [1, 2, 1]
    ats = calculate_ats(res_times, resp_times, first_resp_times)
    expected = 100 / (((10 + 12 + 8)/3 * 0.5) + ((2 + 1 + 3)/3 * 0.2) + ((1 + 2 + 1)/3 * 0.3))
    assert round(ats, 5) == round(expected, 5)


def test_empty_inputs():
    with pytest.raises(ValueError):
        calculate_ats([], [1], [1])

def test_zero_denominator():
    with pytest.raises(ValueError):
        calculate_ats([0], [0], [0])


def test_mismatched_lengths():
    res_times = [10, 15]
    resp_times = [1, 2, 3]
    first_resp_times = [1]
    ats = calculate_ats(res_times, resp_times, first_resp_times)
    expected = 100 / ((12.5 * 0.5) + (2 * 0.2) + (1 * 0.3))
    assert round(ats, 5) == round(expected, 5)


def test_negative_values():
    res_times = [-10, -5]
    resp_times = [-1, -2]
    first_resp_times = [-3]
    ats = calculate_ats(res_times, resp_times, first_resp_times)
    expected = 100 / (((-10 - 5) / 2 * 0.5) + ((-1 - 2) / 2 * 0.2) + (-3 * 0.3))
    assert round(ats, 5) == round(expected, 5)


def test_float_inputs():
    res_times = [10.5, 11.2]
    resp_times = [2.5, 1.3]
    first_resp_times = [1.1, 1.4]
    ats = calculate_ats(res_times, resp_times, first_resp_times)
    expected = 100 / (((10.5 + 11.2) / 2 * 0.5)
                      + ((2.5 + 1.3) / 2 * 0.2)
                      + ((1.1 + 1.4) / 2 * 0.3))
    assert round(ats, 5) == round(expected, 5)

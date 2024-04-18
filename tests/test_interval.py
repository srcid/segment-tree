import pytest

from segment_tree.interval import Interval


@pytest.mark.parametrize('interval, expected_mid, expected_slice', [
    (Interval(0, 6), 3, [1,3,5,7,9,11]),
    (Interval(0, 3), 2, [1,3,5]),
    (Interval(3, 6), 5, [7,9,11]),
    (Interval(0, 2), 1, [1,3]),
    (Interval(2, 3), 3, [5]),
    (Interval(3, 5), 4, [7,9]),
    (Interval(5, 6), 6, [11]),
    (Interval(0, 1), 1, [1]),
    (Interval(1, 2), 2, [3]),
    (Interval(3, 4), 4, [7]),
    (Interval(4, 5), 5, [9])
])
def test_interval(interval: Interval, expected_mid, expected_slice):
    arr = [1,3,5,7,9,11]

    assert interval.mid() == expected_mid
    assert arr[interval.start: interval.end] == expected_slice

def test_interval_copywith_start_2(interval: Interval):
    assert Interval(2, 6) == interval.copyWith(start=2)

def test_interval_copywith_end_5(interval: Interval):
    assert Interval(3, 5) == interval.copyWith(end=5)

def test_interval_copywith_start_0(interval: Interval):
    assert Interval(0, 6) == interval.copyWith(start=0)

def test_interval_dif(interval: Interval):
    assert interval.dif() == 3

def test_interval_isv_true(interval: Interval):
    assert interval.isv() == True

def test_interval_isv_false(interval: Interval):
    assert interval.copyWith(end=3).isv() == False
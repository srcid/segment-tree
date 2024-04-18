import pytest

from segment_tree.interval import Interval


def test_segment_init(arr):
    pass


@pytest.mark.parametrize(
    "interval",
    [
        Interval(0, 1),
        Interval(0, 2),
        Interval(0, 3),
        Interval(0, 4),
        Interval(0, 5),
        Interval(0, 6),
        Interval(1, 2),
        Interval(1, 3),
        Interval(1, 4),
        Interval(1, 5),
        Interval(1, 6),
        Interval(2, 3),
        Interval(2, 4),
        Interval(2, 5),
        Interval(2, 6),
        Interval(3, 4),
        Interval(3, 5),
        Interval(3, 6),
        Interval(4, 5),
        Interval(4, 6),
        Interval(5, 6),
    ],
)
def test_segment_tree_sum(interval, arr, segtree):
    assert segtree.sum(interval) == sum(arr[interval.start : interval.end])

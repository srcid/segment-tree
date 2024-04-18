from io import StringIO

import pytest
import rich

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


def test_segment_tree_as_tree(segtree):
    expected = """36 Interval(start=0, end=6)
├── 9 Interval(start=0, end=3)
│   ├── 4 Interval(start=0, end=2)
│   │   ├── 1 Interval(start=0, end=1)
│   │   └── 3 Interval(start=1, end=2)
│   └── 5 Interval(start=2, end=3)
└── 27 Interval(start=3, end=6)
    ├── 16 Interval(start=3, end=5)
    │   ├── 7 Interval(start=3, end=4)
    │   └── 9 Interval(start=4, end=5)
    └── 11 Interval(start=5, end=6)
"""
    with StringIO() as output:
        rich.print(segtree.asTree(), file=output)
        assert output.getvalue() == expected

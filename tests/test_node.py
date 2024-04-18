import pytest

from segment_tree.interval import Interval
from segment_tree.node import Node


@pytest.mark.parametrize(
    "values, expected",
    [
        ((10, Interval(2, 3), None, None), True),
        ((10, Interval(2, 3)), True),
        ((5, Interval(2, 4), Node(5, Interval(2, 3), None, None), None), False),
        ((5, Interval(3, 5), None, Node(5, Interval(4, 5), None, None)), False),
        (
            (
                10,
                Interval(4, 6),
                Node(5, Interval(4, 5), None, None),
                Node(5, Interval(5, 6), None, None),
            ),
            False,
        ),
    ],
)
def test_node_from_values(values, expected):
    assert Node(*values).isLeaf() == expected

import pytest
from segment_tree.interval import Interval
from segment_tree.segment_tree import SegmentTree

@pytest.fixture
def interval():
    return Interval(3,6)

@pytest.fixture
def arr():
    return [1,3,5,7,9,11]

@pytest.fixture
def segtree(arr):
    return SegmentTree(arr)
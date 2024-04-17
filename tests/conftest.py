import pytest
from segment_tree.interval import Interval

@pytest.fixture
def interval():
    return Interval(3,6)
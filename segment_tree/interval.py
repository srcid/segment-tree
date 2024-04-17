# safe ceiling
# starting with 0
# MID = 1 + (N - 1) // 2
# for a range
# 1 + start + (end - start - 1) // 2 

from __future__ import annotations
from pydantic.dataclasses import dataclass


@dataclass
class Interval():
    start: int
    end: int

    def isv(self) -> bool:
        return self.dif() >= 1
    
    def dif(self) -> int:
        return self.end - self.start
    
    def mid(self) -> int:
        return 1 + self.start + (self.end - self.start - 1) // 2

    def copyWith(self, *, start = None, end = None) -> Interval:
        return Interval(start or self.start, end or self.end)

    def __eq__(self, range) -> bool:
        return self.start == range.start and self.end == range.end

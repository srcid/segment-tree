# safe ceiling
# starting with 0
# MID = 1 + (N - 1) // 2
# for a range
# 1 + start + (end - start - 1) // 2

from __future__ import annotations

from typing import NamedTuple


class Interval(NamedTuple):
    start: int
    end: int

    def isv(self) -> bool:
        return self.dif() >= 1

    def dif(self) -> int:
        return self.end - self.start

    def mid(self) -> int:
        return 1 + self.start + (self.end - self.start - 1) // 2

    def copyWith(self, *, start: int = None, end: int = None) -> Interval:
        return Interval(
            start if start != None else self.start, end if end != None else self.end
        )

from __future__ import annotations

from typing import NamedTuple, Optional

from rich.tree import Tree

from segment_tree.interval import Interval


class Node(NamedTuple):
    key: int
    interval: Interval
    left: Optional[Node] = None
    right: Optional[Node] = None

    def isLeaf(self) -> bool:
        return (self.left, self.right) == (None, None)

    def asTree(self, tree: Tree) -> Tree:
        if self.isLeaf():
            return tree

        leftSubTree = tree.add(f"{self.left.key} {self.left.interval}")
        rightSubTree = tree.add(f"{self.right.key} {self.right.interval}")

        self.left.asTree(leftSubTree)
        self.right.asTree(rightSubTree)

        return tree

    @classmethod
    def fromArr(cls, arr: list, interval: Interval) -> None:
        if interval.dif() == 1:
            return cls(arr[interval.start], interval)

        MID = interval.mid()
        left = Node.fromArr(arr, interval.copyWith(end=MID))
        right = Node.fromArr(arr, interval.copyWith(start=MID))
        key = left.key + right.key

        return cls(key, interval, left, right)

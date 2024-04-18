from segment_tree.interval import Interval
from rich.tree import Tree

class Node:
    def __init__(self, arr: list, interval: Interval) -> None:      
        if interval.dif() == 1:
            self.key = arr[interval.start]
            self.left = None
            self.right = None
        else:
            MID = interval.mid()
            self.left = Node(arr, interval.copyWith(end=MID))
            self.right = Node(arr, interval.copyWith(start=MID))
            self.key = self.left.key + self.right.key

        self.interval = interval

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

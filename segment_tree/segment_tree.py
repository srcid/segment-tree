from time import sleep
from rich.tree import Tree
from rich import print

from segment_tree.interval import Interval
from segment_tree.node import Node

class SegmentTree:
    def __init__(self, arr) -> None:
        self.root = Node(arr, Interval(0, len(arr)))

    def asTree(self) -> str:
        tree = Tree(f'{self.root.key} {self.root.interval}')
        return self.root.asTree(tree)
    
    def sum(self, interval: Interval, node = None):
        node = node or self.root
        
        if not interval.isv():
            return 0
        
        if node.interval == interval:
            return node.key
        
        MID = node.interval.mid()
        
        if interval.end <= MID:
            return self.sum(interval, node.left)
        elif interval.start > MID:
            return self.sum(interval, node.right)
        
        return (
            self.sum(interval.copyWith(end=MID), node.left)
            + self.sum(interval.copyWith(start=MID), node.right)
        )
        

    def insert(e):
        pass
    
    
if __name__ == '__main__':
    #      0, 1, 2, 3, 4, 5, 6
    arr = [1, 3, 5, 7, 9, 11]
    sgt = SegmentTree(arr)

    print(sgt.asTree())
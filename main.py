from rich import print
from segment_tree.segment_tree import SegmentTree


#      0, 1, 2, 3, 4, 5, 6
arr = [1, 3, 5, 7, 9, 11]
sgt = SegmentTree(arr)

print(sgt.asTree())
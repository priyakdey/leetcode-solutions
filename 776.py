"""
776. Split BST

Given the root of a binary search tree (BST) and an integer target, split the 
tree into two subtrees where one subtree has nodes that are all smaller or 
equal to the target value, while the other subtree has all nodes that are 
greater than the target value. It Is not necessarily the case that the tree 
contains a node with the value target.

Additionally, most of the structure of the original tree should remain. 
Formally, for any child c with parent p in the original tree, if they are 
both in the same subtree after the split, then node c should still have the 
parent p.

Return an array of the two roots of the two subtrees.
"""

from typing import List, Optional
from model import TreeNode

# TODO: complete this


class Solution:

    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> List[Optional[TreeNode]]:
        pass

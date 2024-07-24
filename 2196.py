"""
2196. Create Binary Tree From Descriptions

You are given a 2D integer array descriptions where descriptions[i] = [parent_i, 
child_i, isLeft_i] indicates that parenti is the parent of childi in a binary 
tree of unique values. Furthermore,

If isLeft_i == 1, then childi is the left child of parenti.
If isLeft_i == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.
"""

from typing import Dict, List, Optional, Tuple, cast


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if descriptions is None or len(descriptions) == 0 or len(descriptions[0]) != 3:
            raise Exception("invalid arguments")

        tree: Dict[int, Tuple[TreeNode, Optional[TreeNode]]] = {}

        for parent_val, child_val, is_left in descriptions:
            if parent_val not in tree:
                parent = TreeNode(parent_val)
                tree[parent_val] = (parent, None)

            if child_val not in tree:
                child = TreeNode(child_val)
            else:
                child, _ = tree[child_val]

            parent, _ = tree[parent_val]
            if is_left:
                parent.left = child
            else:
                parent.right = child
            tree[child_val] = (child, parent)

        root = None
        for child, parent in tree.values():
            if parent is None:
                root = child
                break

        return root

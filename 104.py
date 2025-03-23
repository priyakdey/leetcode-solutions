from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        max_depth = 0
        if root.left is not None:
            max_depth = max(max_depth, 1 + self.maxDepth(root.left))
        if root.right is not None:
            max_depth = max(max_depth, 1 + self.maxDepth(root.right))

        return max_depth

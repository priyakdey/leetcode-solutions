"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
"""

from typing import Optional
from model import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        max_depth = 0

        def calculate_depth(node: "TreeNode", depth: int) -> None:
            if node.left is None and node.right is None:
                depth += 1
                nonlocal max_depth
                max_depth = max(max_depth, depth)
                return

            if node.left is not None:
                calculate_depth(node.left, depth + 1)
            if node.right is not None:
                calculate_depth(node.right, depth + 1)

        calculate_depth(root, 0)
        return max_depth

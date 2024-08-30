"""
112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the
tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

from typing import Optional

from model import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path_sum(node: Optional[TreeNode], curr_sum: int) -> bool:
            nonlocal targetSum

            if node is None:
                return False
            if node.left is None and node.right is None:
                return node.val + curr_sum == targetSum

            return path_sum(node.left, curr_sum + node.val) or path_sum(
                node.right, curr_sum + node.val
            )

        return path_sum(root, 0)

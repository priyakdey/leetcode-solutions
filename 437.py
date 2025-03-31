from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse(node: Optional[TreeNode], prefix_sum: int) -> None:
            nonlocal count, targetSum

            if node is None:
                return

            if node.val == targetSum:
                count += 1

            if node.val + prefix_sum == targetSum:
                count += 1

            traverse(node.left, prefix_sum + node.val)
            traverse(node.right, prefix_sum + node.val)

        return traverse(root, 0)

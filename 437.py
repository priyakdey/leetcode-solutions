from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse(node: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal count

            if node is None:
                return 0, 0

            left_sum = traverse(node.left)
            right_sum = traverse(node.right)

            if node.val == targetSum:
                count += 1
            if node.val + left_sum == targetSum:
                count += 1
            if node.val + right_sum == targetSum:
                count = +1
            if node.val + left_sum + right_sum == targetSum:
                count += 1

            return node.val + max(left_sum, right_sum)

        count = 0
        traverse(root)
        return count

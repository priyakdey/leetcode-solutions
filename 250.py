"""
250. Count Univalue Subtrees

Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.
"""

from typing import Optional, Tuple

from model import TreeNode


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def traverse(node: TreeNode) -> Tuple[bool, int]:
            nonlocal count

            if node.left is None and node.right is None:
                count += 1
                return True, node.val

            left, right = (True, node.val), (True, node.val)
            if node.left is not None:
                left = traverse(node.left)
            if node.right is not None:
                right = traverse(node.right)

            is_univalue = False
            if left[0] and right[0] and left[1] == right[1] == node.val:
                is_univalue = True
                count += 1

            return is_univalue, node.val

        if root is None:
            return 0

        count: int = 0
        traverse(root)
        return count

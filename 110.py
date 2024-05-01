"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the 
two subtrees of every node never differs by more than one.
"""

from typing import Optional
from model import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: TreeNode) -> int:
            nonlocal max_height_diff

            if node.left is None and node.right is None:
                return 0

            left_subtree_height, right_subtree_height = 0, 0

            if node.left is not None:
                left_subtree_height = 1 + height(node.left)
            if node.right is not None:
                right_subtree_height = 1 + height(node.right)

            max_height_diff = max(
                max_height_diff, abs(left_subtree_height - right_subtree_height)
            )

            return max(left_subtree_height, right_subtree_height)

        if root is None or (root.left is None and root.right is None):
            return True

        max_height_diff = 0
        height(root)
        return max_height_diff <= 1

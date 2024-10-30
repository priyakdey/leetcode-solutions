"""
951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any
node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can
make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two
trees are flip equivalent or false otherwise.
"""

from typing import Optional

from model import TreeNode


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return (
            self.flipEquiv(root1.left, root2.right)
            and self.flipEquiv(root1.right, root2.left)
        ) or (
            self.flipEquiv(root1.left, root2.left)
            and self.flipEquiv(root1.left, root2.right)
        )

"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).
"""

from typing import Optional

from model import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.__is_mirror(root.left, root.right)

    def __is_mirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """__is_mirror returns true if the subtree of the left and right are mirror images"""
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return (
            left.val == right.val
            and self.__is_mirror(left.left, right.right)
            and self.__is_mirror(left.right, right.left)
        )

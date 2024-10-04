"""
156. Binary Tree Upside Down

Given the root of a binary tree, turn the tree upside down and return the new
root.

You can turn a binary tree upside down with the following steps:

- The original left child becomes the new root.
- The original root becomes the new right child.
- The original right child becomes the new left child.
"""
from typing import Optional

from model import TreeNode


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root

        left = self.upsideDownBinaryTree(root.left)
        right = self.upsideDownBinaryTree(root.right)

        root.left, root.right = None, None
        if left is not None:
            left.right = root
            left.left = right
            return root
        else:
            left.left = right
            return root

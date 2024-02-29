"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.
"""

from typing import Optional

from model import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or root.right is None and root.left is None:
            return root

        return self.invert(root)

    def invert(self, node: TreeNode) -> Optional[TreeNode]:
        if node is None:
            return None
        if node.left is None and node.right is None:
            return node

        node.left, node.right = node.right, node.left
        if node.left is not None:
            self.invert(node.left)
        if node.right is not None:
            self.invert(node.right)

        return node

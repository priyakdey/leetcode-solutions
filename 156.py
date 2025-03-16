from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root

        left, right = root.left, root.right
        node = upsideDownBinaryTree(left)
        node.left = upsideDownBinaryTree(right)
        node.right = root
        return node

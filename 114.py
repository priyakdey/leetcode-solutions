"""
114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child 
pointer points to the next node in the list and the left child pointer is 
always null.

The "linked list" should be in the same order as a pre-order traversal of the 
binary tree.
"""
from typing import Optional

from model import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def _flatten(node: TreeNode) -> TreeNode:
            if node.left is None and node.right is None:
                return node

            left, right = None, None

            if node.left is not None:
                left = _flatten(node.left)
            if node.right is not None:
                right = _flatten(node.right)

            if left is not None:
                node.right = left
                curr = node.right
                while curr.right is not None:
                    curr = curr.right
                curr.right = right
            else:
                node.right = right

            node.left = None
            return node

        if root is None:
            return
        _flatten(root)
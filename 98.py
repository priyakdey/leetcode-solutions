"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree 
(BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's 
key. The right subtree of a node contains only nodes with keys greater than 
the node's key. Both the left and right subtrees must also be binary search 
trees.
"""

from typing import Optional

from model import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        return self.is_valid_bst(root, float("-inf"), float("inf"))

    def is_valid_bst(
        self, node: Optional[TreeNode], lower_bound: float, upper_bound: float
    ) -> bool:
        if node is None:
            return True
        return (
            node.val > lower_bound
            and node.val < upper_bound
            and self.is_valid_bst(node.left, lower_bound, float(node.val))
            and self.is_valid_bst(node.right, float(node.val), upper_bound)
        )

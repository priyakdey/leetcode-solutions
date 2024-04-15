"""
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. 
A left leaf is a leaf that is the left child of another node.
"""

from typing import Optional
from model import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0

        return self._sumOfLeftLeaves(root.left, root) + self._sumOfLeftLeaves(
            root.right, root
        )

    def _sumOfLeftLeaves(self, node: TreeNode, parent: TreeNode, sum=0):
        if node is None:
            return 0

        if node.left is None and node.right is None and parent.left == node:
            return sum + node.val

        return (
            sum
            + self._sumOfLeftLeaves(node.left, node, sum)
            + self._sumOfLeftLeaves(node.right, node, sum)
        )

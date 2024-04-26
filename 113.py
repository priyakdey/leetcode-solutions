"""
113. Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf 
paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. 
A leaf is a node with no children.
"""

from typing import List, Optional

from model import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traverse(node: TreeNode, buffer: List[int], total: int) -> None:
            nonlocal targetSum
            nonlocal paths

            if node.left is None and node.right is None:
                if total + node.val == targetSum:
                    buffer.append(node.val)
                    paths.append(list(buffer))
                    buffer.pop()
                return

            buffer.append(node.val)
            if node.left is not None:
                traverse(node.left, buffer, total + node.val)
            if node.right is not None:
                traverse(node.right, buffer, total + node.val)
            buffer.pop()

        if root is None:
            return []

        paths: List[List[int]] = []
        traverse(root, [], 0)
        return paths

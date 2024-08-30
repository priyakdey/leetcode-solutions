"""
145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""
from typing import List, Optional

from model import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node: Optional[TreeNode]) -> None:
            nonlocal nodes

            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            nodes.append(node.val)

        nodes: List[int] = []
        traverse(root)
        return nodes

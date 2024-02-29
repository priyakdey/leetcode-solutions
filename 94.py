"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' 
values.
"""

from typing import List, Optional

from model import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)

        nodes: List[int] = []
        inorder(root)

        return nodes

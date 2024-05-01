"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any 
two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges 
between them.
"""

from typing import Optional, cast

from model import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter

            node = cast(TreeNode, node)

            if node.left is None and node.right is None:
                return 0

            left_height, right_height = 0, 0
            if node.left is not None:
                left_height = 1 + height(node.left)

            if node.right is not None:
                right_height = 1 + height(node.right)

            diameter = left_height + right_height
            if diameter > max_diameter:
                max_diameter = diameter

            return max(left_height, right_height)

        max_diameter = 0
        height(root)
        return max_diameter

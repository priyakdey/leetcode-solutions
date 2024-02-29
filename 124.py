"""
124. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent 
nodes in the sequence has an edge connecting them. A node can only appear in 
the sequence at most once. Note that the path does not need to pass through the 
root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty 
path.
"""

from typing import Optional

from model import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def find_path_sum(node: Optional[TreeNode]) -> int:
            nonlocal max_path_sum

            if node is None:
                return 0
            if node.left is None and node.right is None:
                max_path_sum = max(max_path_sum, node.val)
                return node.val

            left_sum = find_path_sum(node.left)
            right_sum = find_path_sum(node.right)

            max_path_sum = max(
                max_path_sum,
                node.val,
                node.val + left_sum,
                node.val + right_sum,
                node.val + left_sum + right_sum,
            )

            return max(node.val, node.val + left_sum, node.val + right_sum)

        max_path_sum = -(1 << 31)
        find_path_sum(root)
        return max_path_sum

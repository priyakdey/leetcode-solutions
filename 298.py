"""
298. Binary Tree Longest Consecutive Sequence

Given the root of a binary tree, return the length of the longest consecutive 
sequence path.

A consecutive sequence path is a path where the values increase by one along 
the path.

Note that the path can start at any node in the tree, and you cannot go from a 
node to its parent in the path.
"""

from typing import Optional

from model import TreeNode


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        max_streak = 1

        def dfs(node: TreeNode, curr_streak: int) -> None:
            nonlocal max_streak

            max_streak = max(max_streak, curr_streak)

            if node.left is not None:
                if node.val + 1 == node.left.val:
                    dfs(node.left, curr_streak + 1)
                else:
                    dfs(node.left, 1)

            if node.right is not None:
                if node.val + 1 == node.right.val:
                    dfs(node.right, curr_streak + 1)
                else:
                    dfs(node.right, 1)

        dfs(root, 1)
        return max_streak

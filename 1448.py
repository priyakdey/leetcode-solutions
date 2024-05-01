"""
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from 
root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

from typing import Optional
from model import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], max_value: int) -> int:
            count = 0
            if node is None:
                return 0
            if node.val >= max_value:
                max_value = node.val
                count = 1

            return count + dfs(node.left, max_value) + dfs(node.right, max_value)

        if root is None:
            return 1

        return dfs(root, root.val)

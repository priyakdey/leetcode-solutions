"""
2265. Count Nodes Equal to Average of Subtree

Given the root of a binary tree, return the number of nodes where the value 
of the node is equal to the average of the values in its subtree.

Note:

- The average of n elements is the sum of the n elements divided by n and 
  rounded down to the nearest integer.
- A subtree of root is a tree consisting of root and all of its descendants.
"""

from typing import Tuple
from model import TreeNode


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 1

        def dfs(node: TreeNode) -> Tuple[int, int]:
            nonlocal node_count

            if node is None:
                node_count += 1
                return node.val, 1

            total, count = node.val, 1
            if node.left is not None:
                _total, _count = dfs(node.left)
                total += _total
                count += _count
            if node.right is not None:
                _total, _count = dfs(node.right)
                total += _total
                count += _count

            if total // count == node.val:
                node_count += 1

            return total, count

        node_count = 0
        dfs(root)
        return node_count

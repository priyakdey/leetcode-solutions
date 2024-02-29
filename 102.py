"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' 
values. (i.e., from left to right, level by level).
"""

from collections import deque
from typing import Deque, List, Optional, Tuple

from model import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        queue: Deque[Tuple[TreeNode, int]] = deque()
        queue.append((root, 0))

        level_order = []

        while len(queue) != 0:
            node, level = queue.popleft()

            if level >= len(level_order):
                level_order.append([])
            level_order[level].append(node.val)

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

        return level_order

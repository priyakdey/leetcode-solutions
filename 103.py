"""
103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its 
nodes' values. (i.e., from left to right, then right to left for the next level 
and alternate between).
"""

from collections import deque
from typing import Deque, List, Optional, Tuple

from model import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        queue: Deque[Tuple[TreeNode, int]] = deque()
        queue.append((root, 0))

        levels: List[List[int]] = []

        while len(queue) != 0:
            node, level = queue.popleft()
            if len(levels) <= level:
                levels.append([node.val])
            else:
                if level % 2 == 0:
                    levels[level].append(node.val)
                else:
                    levels[level].insert(0, node.val)

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

        return levels

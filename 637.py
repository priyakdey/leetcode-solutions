"""
637. Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each
level in the form of an array. Answers within 10-5 of the actual answer will be
accepted.
"""
from collections import deque
from typing import Deque, List, Optional, Tuple

from model import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]

        levels: List[List[int]] = []

        queue: Deque[Tuple[TreeNode, int]] = deque([(root, 0)])

        while len(queue) > 0:
            node, level = queue.popleft()

            if level >= len(levels):
                levels.append([node.val, 1])
            else:
                levels[level][0] += node.val
                levels[level][1] += 1

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

        return [level[0] / level[1] for level in levels]

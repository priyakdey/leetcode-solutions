"""
429. N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.
"""
from collections import deque
from typing import Deque, List, Optional, Tuple


class Node:
    """Definition for a Node."""

    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        level_order: List[List[int]] = []
        queue: Deque[Tuple[Node, int]] = deque([(root, 0)])

        while len(queue) > 0:
            node, level = queue.popleft()

            if level >= len(level_order):
                level_order.append([])
            level_order[level].append(node.val)

            if node.children:
                for child in node.children:
                    queue.append((child, level + 1))

        return level_order
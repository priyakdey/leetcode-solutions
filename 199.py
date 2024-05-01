"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""

from collections import deque
from typing import Deque, List, Optional, Tuple

from model import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]

        queue: Deque[Tuple[TreeNode, int]] = deque()
        queue.append((root, 0))
        nodes: List[int] = []

        while len(queue) != 0:
            node, level = queue.popleft()
            if level >= len(nodes):
                nodes.append(node.val)
            else:
                nodes[level] = node.val

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

        return nodes

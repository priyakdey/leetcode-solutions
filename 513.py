"""
513. Find Bottom Left Tree Value

Given the root of a binary tree, return the leftmost value in the last row of 
the tree.
"""

from collections import deque
from typing import Deque, Optional, Tuple

from model import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            raise Exception("invalid argument")
        if root.left is None and root.right is None:
            return root.val

        queue: Deque[Tuple[TreeNode, int]] = deque()
        queue.append((root, 0))
        curr_level = 0
        left_most_val = root.val

        while len(queue) != 0:
            node, level = queue.popleft()

            if level > curr_level:
                left_most_val = node.val
                curr_level = level

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

        return left_most_val

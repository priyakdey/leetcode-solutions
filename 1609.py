"""
1609. Even Odd Tree

A binary tree is named Even-Odd if it meets the following conditions:

- The root of the binary tree is at level index 0, its children are at level
  index 1, their children are at level index 2, etc.
- For every even-indexed level, all nodes at the level have odd integer values
  in strictly increasing order (from left to right).
- For every odd-indexed level, all nodes at the level have even integer values
  in strictly decreasing order (from left to right).

Given the root of a binary tree, return true if the binary tree is Even-Odd,
otherwise return false.
"""

from collections import deque
from typing import Deque, List, Optional, Tuple

from model import TreeNode


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            raise Exception("invalid input")
        if root.left is None and root.right is None:
            return root.val % 2 != 0

        levels: List[int] = []
        queue: Deque[Tuple[TreeNode, int]] = deque()
        queue.append((root, 0))

        while len(queue) > 0:
            node, level = queue.popleft()

            if level % 2 == 0 and node.val % 2 == 0:
                return False
            elif level % 2 != 0 and node.val % 2 != 0:
                return False

            if level >= len(levels):
                levels.append(node.val)
            else:
                if level % 2 == 0 and levels[level] >= node.val:
                    return False
                elif level % 2 != 0 and levels[level] <= node.val:
                    return False

                levels[level] = node.val

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

        return True

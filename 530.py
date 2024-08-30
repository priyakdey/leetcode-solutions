"""
530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute
difference between the values of any two different nodes in the tree.
"""

from collections import deque
from typing import Deque, Optional

from model import TreeNode


INT_MAX = (1 << 31) - 1


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack: Deque[TreeNode] = deque()
        curr = root
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        min_diff = INT_MAX
        prev: Optional[TreeNode] = None

        while len(stack) > 0:
            curr = stack.pop()

            node = curr.right
            while node is not None:
                stack.append(node)
                node = node.left

            if prev is not None:
                min_diff = min(min_diff, curr.val - prev.val)
            if len(stack) != 0:
                min_diff = min(min_diff, stack[-1].val - curr.val)

            prev = node

        return min_diff

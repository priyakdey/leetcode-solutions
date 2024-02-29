"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth 
smallest value (1-indexed) of all the values of the nodes in the tree.
"""

from collections import deque
from typing import Deque, Optional

from model import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if k <= 0 or root is None:
            raise Exception("invalid input")
        if root.left is None and root.right is None:
            if k == 1:
                return root.val
            raise Exception("not enough nodes")

        stack: Deque[TreeNode] = deque()
        curr = root
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        while len(stack) != 0:
            curr = stack.pop()

            if k == 1:
                return curr.val

            k -= 1

            child = curr.right
            while child is not None:
                stack.append(child)
                child = child.left

        raise Exception("not enough nodes")

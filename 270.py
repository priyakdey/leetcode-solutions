"""
270. Closest Binary Search Tree Value

Given the root of a binary search tree and a target value, return the value
in the BST that is closest to the target. If there are multiple answers,
print the smallest.
"""

from typing import Optional

from model import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            raise Exception("invalid arguments")

        curr = root
        closest = root.val
        while curr is not None:
            diff = abs(curr.val - target)
            if diff < abs(closest - target):
                closest = curr.val
            elif diff == abs(closest - target):
                closest = min(closest, curr.val)

            if target == curr.val:
                break
            elif target < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return closest

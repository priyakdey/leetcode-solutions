"""
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.
"""

from typing import List, Optional

from model import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_node(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None

            mid = start + (end - start) // 2
            node = TreeNode(nums[mid])
            node.left = create_node(start, mid - 1)
            node.right = create_node(mid + 1, end)
            return node

        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        return create_node(0, len(nums) - 1)

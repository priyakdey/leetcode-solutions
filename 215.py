"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""

# TODO: Reimplement with QuickSelect

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthLargest_heap(nums, k)

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

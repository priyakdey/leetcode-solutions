"""
2541. Minimum Operations to Make Array Equal II

You are given two integer arrays nums1 and nums2 of equal length n and an
integer k. You can perform the following operation on nums1:

Choose two indexes i and j and increment nums1[i] by k and decrement nums1[j]
by k. In other words, nums1[i] = nums1[i] + k and nums1[j] = nums1[j] - k.
nums1 is said to be equal to nums2 if for all indices i such that 0 <= i < n,
nums1[i] == nums2[i].

Return the minimum number of operations required to make nums1 equal to
nums2. If it is impossible to make them equal, return -1.
"""

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if len(nums1) != len(nums2):
            return -1

        negative_diff = 0
        positive_diff = 0
        for i in range(len(nums1)):
            diff = nums1[i] - nums2[i]
            if k != 0 and abs(diff) % k != 0:
                return -1
            if diff < 0:
                negative_diff += diff
            elif diff > 0:
                positive_diff += diff

        if k == 0:
            return 0 if positive_diff == 0 and negative_diff == 0 else -1
        if positive_diff != abs(negative_diff):
            return -1

        return positive_diff // k

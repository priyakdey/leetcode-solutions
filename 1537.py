"""
1537. Get the Maximum Score

You are given two sorted arrays of distinct integers nums1 and nums2.

A valid path is defined as follows:

Choose array nums1 or nums2 to traverse (from index-0).
Traverse the current array from left to right.
If you are reading any value that is present in nums1 and nums2 you are
allowed to change your path to the other array. (Only one repeated value is
considered in the valid path).
The score is defined as the sum of unique values in a valid path.

Return the maximum score you can obtain of all possible valid paths. Since
the answer may be too large, return it modulo 10^9 + 7.
"""

from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # accumulate sum for both arrays till, we have a matching element
        # then consider the largest sum, add the element, and then explore
        # next segment till value is same.
        MOD = 1_000_000_007
        i, j = 0, 0
        sum1, sum2 = 0, 0
        max_sum = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums2[j] < nums1[i]:
                sum2 += nums2[j]
                j += 1
            else:
                max_sum += nums1[i] + max(sum1, sum2)
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1

        while i < len(nums1):
            sum1 += nums1[i]
            i += 1

        while j < len(nums2):
            sum2 += nums2[j]
            j += 1

        max_sum += max(sum1, sum2)
        return max_sum % MOD

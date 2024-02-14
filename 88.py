"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing 
order, and two integers m and n, representing the number of elements in 
nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be 
stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements 
denote the elements that should be merged, and the last n elements are set to 0 
and should be ignored. nums2 has a length of n.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        cursor = m + n - 1

        index1, index2 = m - 1, n - 1

        while index1 >= 0 and index2 >= 0:
            if nums1[index1] >= nums2[index2]:
                nums1[cursor] = nums1[index1]
                index1 -= 1
            else:
                nums1[cursor] = nums2[index2]
                index2 -= 1
            cursor -= 1

        while index2 >= 0:
            nums1[cursor] = nums2[index2]
            index2 -= 1
            cursor -= 1

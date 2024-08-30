"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m == 0 and n == 0:
            return 0.0

        if m == 0:
            mid = n // 2
            if n % 2 == 0:
                return (nums2[mid] + nums2[mid - 1]) / 2
            else:
                return nums2[mid]

        if n == 0:
            mid = m // 2
            if m % 2 == 0:
                return (nums1[mid] + nums1[mid - 1]) / 2
            else:
                return nums1[mid]

        i, j, curr = 1, 0, 0
        mid = (m + n) // 2
        mid_element = nums1[0]

        if nums1[0] > nums2[0]:
            i, j = 0, 1
            mid_element = nums2[0]

        prev_element = -1  # For length == -1, this won't change.
        while i < m and j < n and curr < mid:
            prev_element = mid_element
            if nums1[i] <= nums2[j]:
                mid_element = nums1[i]
                i += 1
            else:
                mid_element = nums2[j]
                j += 1
            curr += 1

        while i < m and curr < mid:
            prev_element = mid_element
            mid_element = nums1[i]
            i += 1
            curr += 1

        while j < n and curr < mid:
            prev_element = mid_element
            mid_element = nums2[j]
            j += 1
            curr += 1

        if (m + n) % 2 == 0:
            return (mid_element + prev_element) / 2
        else:
            return mid_element

"""
2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of 
size 2 where:
- answer[0] is a list of all distinct integers in nums1 which are not present 
  in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present 
  in nums1.

Note that the integers in the lists may be returned in any order.
"""

from typing import List, Set


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [self.difference(nums1, nums2), self.difference(nums2, nums1)]

    def difference(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Returns the difference of nums1 and nums2.
        This method returns a list of distinct integers present in nums1 but not
        in nums2.
            :param: nums1 list of integers
            :param: nums2 list of integers
            :returns: list of integers
        """
        distinct: Set[int] = set(nums2)
        difference: List[int] = []

        for num in nums1:
            if num not in distinct:
                difference.append(num)
                distinct.add(num)  # to avoid duplicates

        return difference

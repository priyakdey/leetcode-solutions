"""
658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest 
integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b
"""

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = self.find_index(arr, x)

        # TODO: Complete this

    def find_index(self, arr: List[int], x: int) -> int:
        """Returns the index of the element x in the array if present, else
        returns the insert position of the element.
        """
        left, right = 0, len(arr) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] >= x:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return index

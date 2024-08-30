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

        if index == 0:
            return arr[:k]
        if index == len(arr):
            return arr[len(arr) - k :]

        i, j = index - 1, index
        elements: List[int] = []

        while i >= 0 and j < len(arr) and k > 0:
            if abs(arr[i] - x) <= abs(arr[j] - x):
                elements.insert(0, arr[i])
                i -= 1
            else:
                elements.append(arr[j])
                j += 1
            k -= 1

        while i >= 0 and k > 0:
            elements.insert(0, arr[i])
            i -= 1
            k -= 1

        while j < len(arr) and k > 0:
            elements.append(arr[j])
            j += 1
            k -= 1

        return elements

    def find_index(self, arr: List[int], x: int) -> int:
        """Returns the index of the element x in the array if present, else
        returns the insertion index. If multiple occurrences, can return any
        index.
        """
        if x < arr[0]:
            return 0
        if x > arr[-1]:
            return len(arr)

        left, right = 0, len(arr) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if x <= arr[mid]:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return index

"""
852. Peak Index in a Mountain Array

An array arr is a mountain if the following properties hold:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
- arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
- arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array arr, return the index i such that 
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2
        peak_index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                peak_index = mid
                break
            elif arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1

        return peak_index

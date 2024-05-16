"""
1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, 
and an integer k.

Return the kth positive integer that is missing from this array.
"""

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1

        # left == right + 1 and kth missing number b/w (arr[right], arr[left])
        # missing numbers left of arr[right] = arr[right] - right - 1
        # arr[right] + k - (arr[right] - right - 1) = k + (right + 1) = k + left
        return k + left

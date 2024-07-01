"""
1550. Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
"""

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if arr is None:
            raise Exception("invalid input")

        if len(arr) < 3:
            return False

        for i in range(len(arr) - 3 + 1):
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True

        return False

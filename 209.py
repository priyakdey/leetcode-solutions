"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return
the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.
"""
from typing import List

INT_MAX = (1 << 31) - 1

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def find_index(arr: List[int], left: int, right: int, target: int) -> int:
            index = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] <= target:
                    index = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        curr_sums: List[int] = [0] * (len(nums) + 1)
        for i in range(1, len(curr_sums)):
            curr_sums[i] = curr_sums[i - 1] + nums[i - 1]

        min_length = INT_MAX

        for i in range(len(curr_sums) - 1, -1, -1):
            compliment = curr_sums[i] - target
            if target < 1:
                break

            index = find_index(curr_sums, 0, i - 1, compliment)
            if index != -1:
                min_length = min(min_length, i - index)

        return min_length if min_length != INT_MAX else 0

"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the 
longest strictly increasing subsequence.
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def find_index_greater_than(target: int) -> int:
            """we need to find the index for an element >= target"""
            index = -1
            left, right = 0, len(subsequence) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if subsequence[mid] >= target:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return index

        subsequence = []
        for num in nums:
            if len(subsequence) == 0:
                subsequence.append(num)
            elif num > subsequence[-1]:
                subsequence.append(num)
            else:
                index = find_index_greater_than(num)
                subsequence[index] = num

        return len(subsequence)

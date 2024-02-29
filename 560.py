"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of 
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

from typing import Dict, List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumm_sum = 0
        lookup_map: Dict[int, int] = {}
        count = 0

        for num in nums:
            cumm_sum += num

            if cumm_sum == k:
                count += 1

            compliment = cumm_sum - k
            if compliment in lookup_map:
                count += lookup_map[compliment]

            if cumm_sum in lookup_map:
                lookup_map[cumm_sum] += 1
            else:
                lookup_map[cumm_sum] = 1

        return count

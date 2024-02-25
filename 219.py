"""
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two 
distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from typing import Dict, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map: Dict[int, int] = {}
        is_pair_found = False

        for i, num in enumerate(nums):
            if num in index_map:
                if abs(i - index_map[num]) <= k:
                    is_pair_found = True
                    break
            index_map[num] = i

        return is_pair_found

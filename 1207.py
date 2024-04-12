"""
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of 
each value in the array is unique or false otherwise.
"""

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_freq_tracker = {}

        for num in arr:
            if num in num_freq_tracker:
                num_freq_tracker[num] += 1
            else:
                num_freq_tracker[num] = 1

        return len(num_freq_tracker.values()) == len(set(num_freq_tracker.values()))

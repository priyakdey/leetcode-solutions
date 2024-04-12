"""
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and 
remove them from the array.

Return the maximum number of operations you can perform on the array.
"""

from typing import Dict, List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq: Dict[int, int] = {}
        max_ops = 0

        for num in nums:
            compliment = k - num
            if compliment in freq:
                max_ops += 1
                freq[compliment] -= 1
                if freq[compliment] == 0:
                    del freq[compliment]
            else:
                if num not in freq:
                    freq[num] = 1
                else:
                    freq[num] += 1

        return max_ops

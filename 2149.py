"""
2149. Rearrange Array Elements by Sign

You are given a 0-indexed integer array nums of even length consisting of an 
equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows 
the given conditions:

- Every consecutive pair of integers have opposite signs.
- For all integers with the same sign, the order in which they were present in 
  nums is preserved.
- The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the 
aforementioned conditions
"""

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) < 2:
            raise Exception("Invalid input")

        odd_idx_ptr, even_idx_ptr = 0, 1
        result: List[int] = [0 for _ in nums]
        for num in nums:
            if num >= 0:
                result[odd_idx_ptr] = num
                odd_idx_ptr += 2
            else:
                result[even_idx_ptr] = num
                even_idx_ptr += 2

        return result

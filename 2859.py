"""
2859. Sum of Values at Indices With K Set Bits

You are given a 0-indexed integer array nums and an integer k.

Return an integer that denotes the sum of elements in nums whose corresponding 
indices have exactly k set bits in their binary representation.

The set bits in an integer are the 1's present when it is written in binary.

For example, the binary representation of 21 is 10101, which has 3 set bits.
"""

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if k == 0:
                return nums[0]
            return 0

        set_bit_count: List[int] = [0 for _ in nums]

        set_bit_count[1] = 1
        prev_power = 1
        for i in range(2, len(set_bit_count)):
            if i == prev_power << 1:
                set_bit_count[i] = 1
                prev_power = prev_power << 1
            else:
                set_bit_count[i] = 1 + set_bit_count[i - prev_power]

        summ = 0
        for i, num in enumerate(nums):
            if set_bit_count[i] == k:
                summ += num

        return summ

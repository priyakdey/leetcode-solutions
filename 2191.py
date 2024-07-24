"""
2191. Sort the Jumbled Numbers

You are given a 0-indexed integer array mapping which represents the mapping 
rule of a shuffled decimal system. mapping[i] = j means digit i should be 
mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each 
occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted 
in non-decreasing order based on the mapped values of its elements.

Notes:
- Elements with the same mapped values should appear in the same relative 
order as in the input.
- The elements of nums should only be sorted based on their mapped values and 
not be replaced by them.
"""

from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_values = sorted(
            map(lambda x: (self.mapToNumber(mapping, x), x), nums), key=lambda x: x[0]
        )
        return [x for _, x in mapped_values]

    def mapToNumber(self, mapping: List[int], num: int) -> int:
        if num == 0:
            return mapping[0]

        mapped_number = 0
        unit = 0
        while num > 0:
            rem = num % 10
            mapped_number = mapped_number + (10**unit) * mapping[rem]
            unit += 1
            num = num // 10

        return mapped_number

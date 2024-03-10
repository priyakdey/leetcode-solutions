"""
1356. Sort Integers by The Number of 1 Bits

You are given an integer array arr. Sort the integers in the array in ascending 
order by the number of 1's in their binary representation and in case of two or 
more integers have the same number of 1's you have to sort them in ascending 
order.

Return the array after sorting it.
"""

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def get_set_count(n: int) -> int:
            set_count = 0
            print(n, end="-")
            for _ in range(32):
                set_count = set_count + (n & 1)
                n = n >> 1
            return set_count

        return sorted(arr, key=lambda n: (get_set_count(n), n))

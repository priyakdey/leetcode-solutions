"""
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are 
not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
and 1 means not empty, and an integer n, return true if n new flowers can be 
planted in the flowerbed without violating the no-adjacent-flowers rule and 
false otherwise.
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return (flowerbed[0] == 0 and n <= 1) or (flowerbed[0] == 1 and n == 0)

        for i in range(len(flowerbed)):
            if n == 0:
                break

            if flowerbed[i] == 0:
                if (
                    (i == 0 and flowerbed[i + 1] == 0)
                    or (i == len(flowerbed) - 1 and flowerbed[i - 1] == 0)
                    or (flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0)
                ):
                    flowerbed[i] = 1
                    n -= 1

        return n == 0

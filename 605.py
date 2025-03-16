from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        if length == 1:
            return (flowerbed[0] == 0 and n <= 1) or (flowerbed[0] == 1 and n == 0)

        for i in range(length):
            if n == 0:
                break

            if flowerbed[i] == 0 and (
                (i == 0 and flowerbed[i + 1] == 0)
                or (i == length - 1 and flowerbed[i - 1] == 0)
                or (flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1

        return n == 0

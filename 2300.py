from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()

        result: List[int] = [0] * len(spells)

        for i, spell in enumerate(spells):
            index = len(potions)
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = left + (right - left) // 2
                product = spell * potions[mid]
                if product >= success:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            result[i] = len(potions) - index

        return result

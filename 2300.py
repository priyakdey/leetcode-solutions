"""
2300. Successful Pairs of Spells and Potions

You are given two positive integer arrays spells and potions, of length n and m 
respectively, where spells[i] represents the strength of the ith spell and 
potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered 
successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of 
potions that will form a successful pair with the ith spell.
"""

from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()

        strong_pairs = [0 for _ in spells]

        for i, spell in enumerate(spells):
            start, end = 0, len(potions) - 1
            found = False
            while start <= end:
                mid = start + (end - start) // 2
                product = spell * potions[mid]
                if product >= success:
                    if mid == 0 or spell * potions[mid - 1] < success:
                        found = True
                        break
                    else:
                        end = mid
                else:
                    start = mid + 1

            if found:
                strong_pairs[i] = len(potions) - mid
            else:
                strong_pairs[i] = 0

        return strong_pairs

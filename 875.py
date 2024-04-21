"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has 
piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses 
some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will 
not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas 
before the guards return.

Return the minimum integer k such that she can eat all the bananas within 
h hours.
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        k = -1

        while low <= high:
            mid = low + (high - low) // 2
            if self.total_time_taken(piles, mid) <= h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1

        return k

    def total_time_taken(self, piles: List[int], k: int) -> int:
        total_time = 0
        for pile in piles:
            total_time += pile // k
            if pile % k != 0:
                total_time += 1

        return total_time

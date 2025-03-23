from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_total_hours(piles: List[int], per_hour: int) -> int:
            total_hours = 0
            for pile in piles:
                total_hours += pile // per_hour
                total_hours += 1 if pile % per_hour != 0 else 0

            return total_hours

        left, right = 1, max(piles)
        per_hour = 0
        while left <= right:
            mid = left + (right - left) // 2
            total_hours = calc_total_hours(piles, mid)
            if total_hours <= h:
                per_hour = mid
                right = mid - 1
            else:
                left = mid + 1

        return per_hour

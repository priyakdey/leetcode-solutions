"""
1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another
within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day,
we load the ship with packages on the conveyor belt (in the order given by
weights). We may not load more weight than the maximum weight capacity of the
ship.

Return the least weight capacity of the ship that will result in all the
packages on the conveyor belt being shipped within days days.
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_capacity, max_capacity = max(weights), sum(weights)

        capacity = max_capacity
        while min_capacity <= max_capacity:
            mid = min_capacity + (max_capacity - min_capacity) // 2
            reqd_days = self.calc_days(weights, mid)
            if reqd_days <= days:
                capacity = mid
                max_capacity = mid - 1
            else:
                min_capacity = mid + 1

        return capacity

    def calc_days(self, weights: List[int], capacity: int) -> int:
        days = 1
        curr_weight = 0
        for weight in weights:
            if curr_weight + weight > capacity:
                days += 1
                curr_weight = 0
            curr_weight += weight

        return days

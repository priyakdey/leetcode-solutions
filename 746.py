from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        next1, next2 = cost[-1], cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            curr = min(next1, next2) + cost[i]
            next1, next2 = next2, curr

        return min(next1, next2)

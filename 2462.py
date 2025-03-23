from heapq import heappop, heappush
from typing import List


class Pair:

    def __init__(self, cost: int, index: int) -> None:
        self.cost = cost
        self.index = index

    def __lt__(self, other: "Pair") -> bool:
        if self.cost == other.cost:
            return self.index < other.index
        return self.cost < other.cost


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        min_heap: List[Pair] = []
        total_cost = 0

        if len(costs) < 2 * candidates:
            for i, cost in enumerate(costs):
                heappush(min_heap, Pair(cost, i))

            while k > 0:
                pair = heappop(min_heap)
                total_cost += pair.cost
                k -= 1

            return total_cost

        left, right = 0, len(costs) - 1
        for i in range(candidates):
            heappush(min_heap, Pair(costs[left], left))
            left += 1

        for i in range(candidates):
            heappush(min_heap, Pair(costs[right], right))
            right -= 1

        while k > 0:
            pair = heappop(min_heap)
            total_cost += pair.cost

            if left > right:
                pass
            elif pair.index >= right:
                heappush(min_heap, Pair(costs[right], right))
                right -= 1
            else:
                heappush(min_heap, Pair(costs[left], left))
                left += 1
            k -= 1

        return total_cost

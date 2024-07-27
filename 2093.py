"""
2093. Minimum Cost to Reach City With Discounts

A series of highways connect n cities numbered from 0 to n - 1. You are given a
2D integer array highways where highways[i] = [city1i, city2i, tolli] indicates
that there is a highway that connects city1i and city2i, allowing a car to go
from city1i to city2i and vice versa for a cost of tolli.

You are also given an integer discounts which represents the number of discounts
you have. You can use a discount to travel across the ith highway for a cost of
tolli / 2 (integer division). Each discount may only be used once, and you can
only use at most one discount per highway.

Return the minimum total cost to go from city 0 to city n - 1, or -1 if it is
not possible to go from city 0 to city n - 1.
"""

import heapq
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(list)
        for city1, city2, toll in highways:
            graph[city1].append((city2, toll))
            graph[city2].append((city1, toll))

        pq = [(0, 0, discounts)]

        cost = defaultdict(lambda: inf)
        cost[(0, discounts)] = 0

        min_cost = -1

        while pq:
            curr_cost, city, discounts_left = heapq.heappop(pq)

            if city == n - 1:
                min_cost = curr_cost
                break
            elif curr_cost > cost[(city, discounts_left)]:
                continue

            for neighbor, toll in graph[city]:
                # do not take a discount
                new_cost = curr_cost + toll
                if new_cost < cost[(neighbor, discounts_left)]:
                    cost[(neighbor, discounts_left)] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, discounts_left))

                # try and take a discount
                if discounts_left > 0:
                    discounted_cost = curr_cost + toll // 2
                    if discounted_cost < cost[(neighbor, discounts_left - 1)]:
                        cost[(neighbor, discounts_left - 1)] = discounted_cost
                        heapq.heappush(
                            pq, (discounted_cost, neighbor, discounts_left - 1)
                        )

        return min_cost

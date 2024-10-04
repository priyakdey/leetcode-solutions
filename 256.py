"""
256. Paint House

There is a row of n houses, where each house can be painted one of three colors:
red, blue, or green. The cost of painting each house with a certain color is
different. You have to paint all the houses such that no two adjacent houses
have the same color.

The cost of painting each house with a certain color is represented by an n x 3
cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red;
costs[1][2] is the cost of painting house 1 with color green, and so on...

Return the minimum cost to paint all houses.
"""

from typing import List

INT_MAX = (1 << 31) - 1


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        rows, cols = len(costs), 3
        min_cost_prev_row: List[int] = costs[0]
        min_cost_curr_row: List[int] = [0] * cols

        for row in range(1, rows):
            min_cost_curr_row[0] = costs[row][0] + min(
                min_cost_prev_row[1], min_cost_prev_row[2]
            )
            min_cost_curr_row[1] = costs[row][1] + min(
                min_cost_prev_row[0], min_cost_prev_row[2]
            )
            min_cost_curr_row[2] = costs[row][2] + min(
                min_cost_prev_row[0], min_cost_prev_row[1]
            )

            for i in range(cols):
                min_cost_prev_row[i] = min_cost_curr_row[i]

        return min(min_cost_prev_row)

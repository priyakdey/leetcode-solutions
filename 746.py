"""
746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a 
staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost_one_next_step = cost[-1]
        min_cost_two_next_step = cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            min_cost_curr_step = cost[i] + min(
                min_cost_one_next_step, min_cost_two_next_step
            )
            min_cost_one_next_step = min_cost_two_next_step
            min_cost_two_next_step = min_cost_curr_step

        return min(min_cost_one_next_step, min_cost_two_next_step)

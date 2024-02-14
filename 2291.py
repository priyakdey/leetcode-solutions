"""
2291. Maximum Profit From Trading Stocks

You are given two 0-indexed integer arrays of the same length present and future 
where present[i] is the current price of the ith stock and future[i] is the 
price of the ith stock a year in the future. 
You may buy each stock at most once. 
You are also given an integer budget representing the amount of money you 
currently have.

Return the maximum amount of profit you can make.
"""

from typing import List


class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        cache: List[List[int]] = [[-1 for _ in range(budget + 1)] for _ in present]
        # return self.maximum_profit_rec(present, future, 0, budget, cache)
        return self.maximum_profit_tab(present, future, budget)

    def maximum_profit_tab(
        self, present: List[int], future: List[int], budget: int
    ) -> int:
        cache: List[List[int]] = [
            [-1 for _ in range(budget + 1)] for _ in range(len(present) + 1)
        ]

        cache[-1] = [0] * budget
        for i in range(len(present) - 1, -1, -1):
            for j in range(0, budget + 1):
                max_profit = cache[i + 1][j]
                profit_from_this_stock = future[i] - present[i]
                if profit_from_this_stock > 0 and j >= present[i]:
                    max_profit = max(
                        max_profit,
                        profit_from_this_stock + cache[i + 1][j - present[i]],
                    )
                cache[i][j] = max_profit

        return cache[0][0]

    def maximum_profit_rec(
        self,
        present: List[int],
        future: List[int],
        index: int,
        budget: int,
        cache: List[List[int]],
    ) -> int:
        if index == len(present):
            return 0

        if cache[index][budget] != -1:
            return cache[index][budget]

        # Option 1: Skip this stock
        max_profit = self.maximum_profit_rec(present, future, index + 1, budget, cache)

        # Option 2: Buy this stock if profitable and budget allows
        profit_from_this_stock = future[index] - present[index]
        if profit_from_this_stock > 0 and budget >= present[index]:
            max_profit = max(
                max_profit,
                profit_from_this_stock
                + self.maximum_profit_rec(
                    present, future, index + 1, budget - present[index], cache
                ),
            )

        cache[index][budget] = max_profit
        return max_profit

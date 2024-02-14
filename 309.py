"""
309. Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock 
on the ith day.

Find the maximum profit you can achieve. 
You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with the 
following restrictions:

After you sell your stock, you cannot buy stock on the next day 
(i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cache: List[int] = [-1 for _ in prices]
        # return self._maxProfitRec(prices, 0, cache)
        return self._maxProfitTab(prices)

    def _maxProfitTab(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # cache[i] represents the max profit from day i to the end
        cache = [0 for _ in range(n + 2)]  # Padding to handle cooldown

        for i in range(n - 1, -1, -1):
            max_profit = 0
            # Option 1: Do not buy on day i
            max_profit = cache[i + 1]
            # Option 2: Buy on day i and sell on a future day j
            for j in range(i + 1, n):
                profit = (
                    prices[j] - prices[i] + cache[j + 2]
                )  # Cooldown period accounted for
                max_profit = max(max_profit, profit)
            cache[i] = max_profit

        return cache[0]

    def _maxProfitRec(self, prices: List[int], index: int, cache: List[int]) -> int:
        if index >= len(prices):
            return 0

        if cache[index] != -1:
            return cache[index]

        # do not buy today
        max_profit = self._maxProfitRec(prices, index + 1, cache)

        # buy today and book profit for next days
        buy_price = prices[index]
        for i in range(index + 1, len(prices)):
            sell_price = prices[i]
            profit = sell_price - buy_price + self._maxProfitRec(prices, i + 2, cache)
            max_profit = max(max_profit, profit)

        cache[index] = max_profit
        return max_profit

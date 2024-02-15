"""
122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given 
stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 1:
            return 0

        buying_price = prices[0]
        profit = 0
        for i in range(1, length):
            if prices[i] >= buying_price:
                profit += prices[i] - buying_price
            buying_price = prices[i]

        return profit

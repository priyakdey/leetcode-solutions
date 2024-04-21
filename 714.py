"""
714. Best Time to Buy and Sell Stock with Transaction Fee

You are given an array prices where prices[i] is the price of a given stock on 
the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions 
as you like, but you need to pay the transaction fee for each transaction.

Note:
- You may not engage in multiple transactions simultaneously 
  (i.e., you must sell the stock before you buy again).
- The transaction fee is only charged once for each stock purchase and sale.
"""

from typing import List

# TODO: Complete this

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pass
    def max_profit(self, prices: List[int], index: int, buy_price: int, n: int, fee: int) -> int:
        if index == len(prices):
            return 0

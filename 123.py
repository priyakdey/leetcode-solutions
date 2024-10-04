"""
123. Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on 
the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).
"""

from typing import Dict, List, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def calc_max_profit(
            index: int,
            share: int,
            buy_price: int,
            tx: int,
            cache: Dict[Tuple[int, int, int, int], int],
        ) -> int:
            nonlocal prices

            if index == len(prices) or tx == 0:
                return 0

            key = (index, share, buy_price, tx)
            if key in cache:
                return cache[key]

            if share == 0:
                # do not buy
                profit = calc_max_profit(index + 1, 0, -1, tx, cache)
                # buy the share
                profit = max(
                    profit, calc_max_profit(index + 1, 1, prices[index], tx, cache)
                )
            else:
                # do not sell
                profit = calc_max_profit(index + 1, 1, buy_price, tx, cache)
                profit = max(
                    profit,
                    prices[index]
                    - buy_price
                    + calc_max_profit(index + 1, 0, -1, tx - 1, cache),
                )

            cache[key] = profit
            return profit

        cache: Dict[Tuple[int, int, int, int], int] = {}
        return calc_max_profit(0, 0, -1, 2, cache)

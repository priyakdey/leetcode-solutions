"""
322. Coin Change

You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, 
return -1.

You may assume that you have an infinite number of each kind of coin.
"""

from typing import List


INT_MAX = (1 << 31) - 1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache: List[List[int]] = [
            [-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)
        ]
        count = self.coin_change(coins, 0, amount, cache)
        return count if count != INT_MAX else -1

    def coin_change(
        self, coins: List[int], index: int, amount: int, cache: List[List[int]]
    ) -> int:
        if amount == 0:
            return 0

        if amount < 0 or index == len(coins):
            return INT_MAX

        if cache[index][amount] != -1:
            return cache[index][amount]

        count = INT_MAX

        for i in range(index, len(coins)):
            c = self.coin_change(coins, i, amount - coins[i], cache)
            if c != INT_MAX:
                count = min(count, 1 + c)

        cache[index][amount] = count
        return count

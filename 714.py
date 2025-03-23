from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @lru_cache(maxsize=None)
        def dp(i: int, holding: int) -> int:
            if i == n:
                return 0

            if holding:
                # Two choices: sell or hold
                return max(prices[i] - fee + dp(i + 1, 0), dp(i + 1, 1))
            else:
                # Two choices: buy or skip
                return max(-prices[i] + dp(i + 1, 1), dp(i + 1, 0))

        return dp(0, 0)

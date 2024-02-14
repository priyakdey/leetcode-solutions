"""
441. Arranging Coins

You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you 
will build.
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        row = -1
        while left <= right:
            mid = left + (right - left) // 2
            total_coins = mid * (mid + 1) // 2
            if total_coins <= n:
                row = mid
                left = mid + 1
            else:
                right = mid - 1

        return row

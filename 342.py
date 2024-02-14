"""
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

# TODO: Follow up: Could you solve it without loops/recursion?


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return self.is_power_of_four(1, abs(n))

    def is_power_of_four(self, curr: int, n: int) -> bool:
        if curr == n:
            return True
        if curr > n:
            return False
        return self.is_power_of_four(curr * 4, n)

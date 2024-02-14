"""
326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""

# TODO: Follow up: Could you solve it without loops/recursion?


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return self.is_power_of_three(1, n)

    def is_power_of_three(self, curr: int, n: int) -> bool:
        if curr == n:
            return True
        if curr > n:
            return False
        return self.is_power_of_three(curr * 3, n)

"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

# TODO: Follow up: Could you solve it without loops/recursion?


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return self.is_power_of_two(1, abs(n))

    def is_power_of_two(self, curr: int, n: int) -> bool:
        if curr == n:
            return True
        if curr > n:
            return False
        return self.is_power_of_two(curr * 2, n)

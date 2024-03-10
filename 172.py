"""
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        for i in range(5, n + 1, 5):
            curr = i
            while curr % 5 == 0:
                count += 1
                curr = curr // 5

        return count

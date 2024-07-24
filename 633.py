"""
633. Sum of Square Numbers

Given a non-negative integer c, decide whether there are two integers a and b
such that a^2 + b^2 = c.
"""

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, math.floor(math.sqrt(c))
        while left <= right:
            x = left * left + right * right
            if x == c:
                return True
            elif x < c:
                left += 1
            else:
                right -= 1

        return False

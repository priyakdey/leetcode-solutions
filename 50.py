"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == -1:
            return 1 if n % 2 == 0 else -1

        if n == 1:
            return x
        if n == 0:
            return 1
        if n == -1:
            return 1 / x
        if n == 2:
            return x * x
        if n == -2:
            return 1 / (x * x)

        is_negative = n < 0
        power = self.pow(x, abs(n))
        if is_negative:
            return 1 / power
        return power

    def pow(self, x: float, n: int) -> float:
        if n == 1:
            return x

        p = self.pow(x, n // 2)
        if n % 2 == 0:
            return self.myPow(p, 2)
        else:
            return x * self.myPow(p, 2)

"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        power = self.pow(x, abs(n))
        if n < 0:
            return 1 / power
        else:
            return power

    def pow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        k = n // 2
        power = self.pow(x, k)
        if n % 2 != 0:
            return power * power * x
        else:
            return power * power

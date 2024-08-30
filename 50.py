"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x: float, n: int) -> float:
            if n == 1:
                return x
            result = pow(x, n // 2)
            if n & 1 == 0:
                return result * result
            else:
                return x * result * result

        if n == 1:
            return x
        if n == -1:
            return 1 / x
        if n == 0:
            return 1.0
        if x == 1.0:
            return 1.0
        if x == -1.0:
            return -1.0 if n & 1 == 1 else 1.0


        negative = n < 0
        result = pow(x, abs(n))
        return result if not negative else  (1 / result)

"""
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using
multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its
fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would
be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−2 ^ 31, 2 ^ 31 − 1]. For this problem,
if the quotient is strictly greater than 2 ^ 31 - 1, then return 2 ^ 31 - 1,
and if the quotient is strictly less than -2 ^ 31, then return -2 ^ 31.
"""

INT_MAX, INT_MIN = (1 << 31) - 1, -(1 << 31)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive: bool = (dividend > 0 and divisor > 0) or (
            dividend < 0 and divisor < 0
        )
        dividend = abs(dividend) if dividend != INT_MIN else INT_MAX
        divisor = abs(divisor) if divisor != INT_MIN else INT_MAX

        quotient: int = 0

        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                quotient += 1 << i

        return quotient if positive else -quotient
"""
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        one, two, three = 0, 1, 1

        if n == 0:
            return one
        if n == 1:
            return two
        if n == 2:
            return three

        for _ in range(3, n + 1):
            one, two, three = two, three, one + two + three

        return three

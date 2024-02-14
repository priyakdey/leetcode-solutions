"""
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
Fibonacci sequence, such that each number is the sum of the two preceding ones, 
starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""


from typing import Dict


class Solution:
    def fib(self, n: int) -> int:
        return self.fib_with_memo(n, {})

    def fib_with_memo(self, n: int, cache: Dict[int, int]) -> int:
        if n <= 1:
            return n
        if n in cache:
            return cache[n]
        fib_n = self.fib(n - 1) + self.fib(n - 2)
        cache[n] = fib_n
        return fib_n

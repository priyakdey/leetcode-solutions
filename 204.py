"""
204. Count Primes

Given an integer n, return the number of prime numbers that are strictly less 
than n.
"""

from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime: List[bool] = [True for _ in range(n)]
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)

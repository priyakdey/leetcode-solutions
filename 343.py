"""
343. Integer Break

Given an integer n, break it into the sum of k positive integers, where k >= 2, 
and maximize the product of those integers.

Return the maximum product you can get.
"""

from typing import Dict, Tuple


class Solution:
    def integerBreak(self, n: int) -> int:

        def integer_break(n: int, k: int) -> int:
            nonlocal max_product
            nonlocal cache

            if n == 0:
                return 1 if k >= 2 else -1

            if n < 0:
                return -1

            if (n, k) in cache:
                return cache[n, k]

            product = -1

            for i in range(1, n + 1):
                _product = integer_break(n - i, k + 1)
                if _product != -1:
                    product = max(product, _product * i)
                    max_product = max(max_product, product)

            cache[(n, k)] = product
            return product

        max_product = 0
        cache: Dict[Tuple[int, int], int] = {}

        integer_break(n, 0)
        return max_product

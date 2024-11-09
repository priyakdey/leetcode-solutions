"""
397. Integer Replacement

Given a positive integer n, you can apply one of the following operations:

- If n is even, replace n with n / 2.
- If n is odd, replace n with either n + 1 or n - 1.

Return the minimum number of operations needed for n to become 1.
"""
from typing import Dict


INT_MAX = (1 << 31) - 1


class Solution:
    def integerReplacement(self, n: int) -> int:
        def sim_operations(num: int, cache: Dict[int, int]) -> int:
            if num == 1:
                return 0
            elif num < 1:
                return INT_MAX

            if num in cache:
                return cache[num]

            operations = INT_MAX

            if num & 1 == 0:
                op = sim_operations(num // 2, cache)
                if op != INT_MAX:
                    operations = min(operations, 1 + op)
            else:
                op = sim_operations(num + 1, cache)
                if op != INT_MAX:
                    operations = min(operations, 1 + op)

                op = sim_operations(num - 1, cache)
                if op != INT_MAX:
                    operations = min(operations, 1 + op)

            cache[num] = operations
            return operations

        return sim_operations(n, {})

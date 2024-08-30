"""
2998. Minimum Number of Operations to Make X and Y Equal

You are given two positive integers x and y.

In one operation, you can do one of the four following operations:

1. Divide x by 11 if x is a multiple of 11.
2. Divide x by 5 if x is a multiple of 5.
3. Decrement x by 1.
4. Increment x by 1.

Return the minimum number of operations required to make x and y equal.
"""

from typing import Dict


INT_MAX = (1 << 31) - 1


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x < y:
            return y - x

        return self.min_moves(x, y, {})

    def min_moves(self, x: int, y: int, cache: Dict[int, int]) -> int:
        if x == y:
            return 0

        if x < y:
            return INT_MAX

        if x in cache:
            return cache[x]

        moves = 1 + self.min_moves(x - 1, y, cache)
        moves = min(moves, 1 + self.min_moves(x + 1, y, cache))

        if x % 11 == 0:
            min_moves = self.min_moves(x // 11, y, cache)
            if min_moves != INT_MAX:
                moves = min(moves, 1 + min_moves)
        elif x % 5 == 0:
            min_moves = self.min_moves(x // 5, y, cache)
            if min_moves != INT_MAX:
                moves = min(moves, 1 + min_moves)

        cache[x] = moves
        return moves

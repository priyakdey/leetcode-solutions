"""
650. 2 Keys Keyboard

There is only one character 'A' on the screen of a notepad. You can perform
one of two operations on this notepad for each step:

- Copy All: You can copy all the characters present on the screen
  (a partial copy is not allowed).
- Paste: You can paste the characters which are copied last time.

Given an integer n, return the minimum number of operations to get the
character 'A' exactly n times on the screen.
"""

from typing import List, Optional


INT_MAX = (1 << 31) - 1


class Solution:
    def minSteps(self, n: int) -> int:
        def steps(curr: int, clipboard: int, cache: List[List[Optional[int]]]) -> int:
            if curr == n:
                return 0

            if curr > n:
                return INT_MAX

            if cache[curr][clipboard] is not None:
                return cache[curr][clipboard]

            min_steps = INT_MAX

            # paste things from clipboard and move along
            min_steps = min(min_steps, 1 + steps(curr + clipboard, clipboard, cache))

            # copy all elements and paste that
            min_steps = min(min_steps, 2 + steps(curr + curr, curr, cache))

            cache[curr][clipboard] = min_steps
            return min_steps

        if n == 1:
            return 0

        cache: List[List[Optional[int]]] = [
            [None for _ in range(n + 1)] for _ in range(n + 1)
        ]
        return 1 + steps(1, 1, cache)

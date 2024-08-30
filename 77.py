"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].

You may return the answer in any order.
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        buf: List[int] = [0] * k
        acc: List[List[int]] = []
        self.generate(buf, 0, 0, n, k, acc)
        return acc

    def generate(
        self,
        buf: List[int],
        index: int,
        curr: int,
        n: int,
        k: int,
        acc: List[List[int]],
    ) -> None:
        if index == k:
            acc.append(list(buf))
            return

        if curr > n:
            return

        for i in range(curr + 1, n + 1):
            buf[index] = i
            self.generate(buf, index + 1, i, n, k, acc)

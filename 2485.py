"""
2485. Find the Pivot Integer

Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements 
between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. 
It is guaranteed that there will be at most one pivot index for the given input.
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        if n < 1:
            raise Exception("invalid input")

        for i in range(1, n + 1):
            if self.sum(1, i) == self.sum(i, n):
                return i

        return -1

    def sum(self, start: int, end: int) -> int:
        return ((end * (end + 1)) - ((start - 1) * start)) // 2

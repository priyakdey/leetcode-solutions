"""
2028. Find Missing Observations

You have observations of n + m 6-sided dice rolls with each face numbered
from 1 to 6. n of the observations went missing, and you only have the
observations of m rolls. Fortunately, you have also calculated the average
value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of
the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the
average value of the n + m rolls is exactly mean. If there are multiple valid
answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible
by n + m.
"""

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = (len(rolls) + n) * mean
        rolls_total = sum(rolls)

        diff = total - rolls_total

        result: List[int] = [1] * n
        left = diff - n
        i = 0
        while i < n and left > 0:
            result[i] = min(6, 1 + left)
            left = left - (result[i] - 1)
            i += 1

        return result if left == 0 else []

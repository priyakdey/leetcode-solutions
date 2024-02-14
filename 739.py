"""
739. Daily Temperatures
Solved
Medium
Topics
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: Deque[Tuple[int, int]] = deque()
        answer = [0 for _ in temperatures]

        for i, temperature in enumerate(temperatures):
            while len(stack) != 0 and temperature > stack[-1][0]:
                popped = stack.pop()
                index = popped[1]
                answer[index] = i - index

            stack.append((temperature, i))

        return answer

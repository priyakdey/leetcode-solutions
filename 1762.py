"""
1762. Buildings With an Ocean View

There are n buildings in a line. You are given an integer array heights of size 
n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the 
building can see the ocean without obstructions. Formally, a building has an 
ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, 
sorted in increasing order.
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack: Deque[Tuple[int, int]] = deque()

        for index, height in enumerate(heights):
            while len(stack) != 0 and height >= stack[-1][0]:
                stack.pop()
            stack.append((height, index))

        indices: List[int] = [-1] * len(stack)
        cursor = 0
        while len(stack) != 0:
            indices[cursor] = stack.popleft()[1]
            cursor += 1

        return indices

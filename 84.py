"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest rectangle in 
the histogram.
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right_bound_index = [len(heights) for _ in heights]

        stack: Deque[Tuple[int, int]] = deque()

        for i in range(len(heights)):
            height = heights[i]
            while len(stack) != 0 and height < stack[-1][0]:
                right_bound_index[stack.pop()[1]] = i

            stack.append((height, i))

        left_bound_index = [-1 for _ in heights]
        stack.clear()

        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]
            while len(stack) != 0 and height < stack[-1][0]:
                left_bound_index[stack.pop()[1]] = i
            stack.append((height, i))

        max_area = 0
        for i, height in enumerate(heights):
            breadth = (right_bound_index[i] - 1) - (left_bound_index[i] + 1) + 1
            area = height * breadth
            max_area = max(max_area, area)

        return max_area

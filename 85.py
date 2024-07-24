"""
85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest 
rectangle containing only 1's and return its area.
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        heights: List[List[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "0":
                    heights[row][col] = 0
                else:
                    if row == 0:
                        heights[row][col] = int(matrix[row][col])
                    else:
                        heights[row][col] = 1 + heights[row - 1][col]

        stack: Deque[Tuple[int, int]] = deque()
        max_area = 0

        for row in range(rows):
            area = self.calc_max_area(heights[row], rows, cols, stack)
            max_area = max(max_area, area)

        return max_area

    def calc_max_area(
        self, heights: List[int], rows: int, cols: int, stack: Deque[Tuple[int, int]]
    ) -> int:

        right_bound = [cols - 1] * cols
        for i, height in enumerate(heights):
            while len(stack) != 0 and height < stack[-1][0]:
                _, index = stack.pop()
                right_bound[index] = i - 1
            stack.append((height, i))

        stack.clear()

        left_bound = [0] * cols
        for i in range(cols - 1, -1, -1):
            height = heights[i]
            while len(stack) != 0 and height < stack[-1][0]:
                _, index = stack.pop()
                left_bound[index] = i + 1
            stack.append((height, i))

        stack.clear()

        max_area = 0
        for i in range(cols):
            width = (right_bound[i] - left_bound[i] + 1) * 1
            height = heights[i]
            area = height * width
            max_area = max(max_area, area)

        return max_area

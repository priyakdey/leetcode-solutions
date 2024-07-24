"""
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and
Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n
integer matrix heights where heights[r][c] represents the height above sea
level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring
cells directly north, south, east, and west if the neighboring cell's height
is less than or equal to the current cell's height. Water can flow from any
cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes
that rain water can flow from cell (ri, ci) to both the Pacific
and Atlantic oceans.
"""

from collections import deque
from typing import List, Set, Tuple, Deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        can_flow_to_pacific = [[False for _ in range(cols)] for _ in range(rows)]
        can_flow_to_atlantic = [[False for _ in range(cols)] for _ in range(rows)]

        visited: Set[Tuple[int, int]] = set()
        queue: Deque[Tuple[int, int]] = deque()
        directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue.append((0, 0))
        visited.add((0, 0))

        while len(queue) > 0:
            row, col = queue.popleft()
            can_flow_to_pacific[row][col] = True

            for dx, dy in directions:
                r, c = row + dx, col + dy
                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and (r, c) not in visited
                    and heights[r][c] >= heights[row][col]
                ):
                    queue.append((r, c))
                    visited.add((r, c))

        visited.clear()
        queue.clear()

        queue.append((rows - 1, cols - 1))
        visited.add((rows - 1, cols - 1))
        while len(queue) > 0:
            row, col = queue.popleft()
            can_flow_to_atlantic[row][col] = True

            for dx, dy in directions:
                r, c = row + dx, col + dy
                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and (r, c) not in visited
                    and heights[r][c] >= heights[row][col]
                ):
                    queue.append((r, c))
                    visited.add((r, c))

        indices: List[List[int]] = []

        for row in range(rows):
            for col in range(cols):
                if can_flow_to_pacific[row][col] and can_flow_to_atlantic[row][col]:
                    indices.append([row, col])

        return indices

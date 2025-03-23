from collections import deque
from typing import Deque, List, Set


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        INT_MAX = (1 << 31) - 1
        directions: List[Tuple[int, int]] = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        queue: Deque[Tuple[int, int, int]] = deque()
        visited: Set[Tuple[int, int]] = set()
        min_distance = INT_MAX
        queue.append((entrance[0], entrance[1], 0))
        visited.add((entrance[0], entrance[1]))

        while len(queue) > 0:
            row, col, dist = queue.popleft()

            if [row, col] != entrance:
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    min_distance = min(min_distance, dist)

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and maze[next_row][next_col] == "."
                    and (next_row, next_col) not in visited
                ):
                    print(next_row, next_col)
                    queue.append((next_row, next_col, dist + 1))
                    visited.add((next_row, next_col))

        return min_distance if min_distance != INT_MAX else -1

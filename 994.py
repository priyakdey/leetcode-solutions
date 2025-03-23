from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue: Deque[Tuple[int, int, int]] = deque()
        fresh_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                if grid[row][col] == 1:
                    fresh_count += 1

        min_minute = 0

        while len(queue) != 0:
            row, col, minute = queue.popleft()

            min_minute = max(min_minute, minute)

            if row - 1 >= 0 and grid[row - 1][col] == 1:
                queue.append((row - 1, col, minute + 1))
                grid[row - 1][col] = 2
                fresh_count -= 1

            if row + 1 < rows and grid[row + 1][col] == 1:
                queue.append((row + 1, col, minute + 1))
                grid[row + 1][col] = 2
                fresh_count -= 1

            if col - 1 >= 0 and grid[row][col - 1] == 1:
                queue.append((row, col - 1, minute + 1))
                grid[row][col - 1] = 2
                fresh_count -= 1

            if col + 1 < cols and grid[row][col + 1] == 1:
                queue.append((row, col + 1, minute + 1))
                grid[row][col + 1] = 2
                fresh_count -= 1

        return min_minute if fresh_count == 0 else -1

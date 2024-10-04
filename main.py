from typing import List, Set


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for row in grid:
            row.sort(reverse=True)

        seen: Set[int] = set()
        max_value: int = 0

        for col in range(cols):
            value = grid[0][col]
            seen.add(grid[0][col])

            for row in range(1, rows):
                for c in range(cols):
                    if grid[row][c] not in seen:
                        value += grid[row][c]
                        seen.add(grid[row][c])
                        break

            max_value = max(max_value, value)
            seen.clear()

        return max_value

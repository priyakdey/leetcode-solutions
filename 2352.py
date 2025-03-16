from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        assert rows == cols, "According to constraints"

        pairs = 0

        for row in range(rows):
            is_same = True
            for col in range(cols):
                if grid[row][col] != grid[col][row]:
                    is_same = False
                    break

            pairs += 1 if is_same else 0

        return pairs

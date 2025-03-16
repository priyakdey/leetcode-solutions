from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        elements = n * n
        expected_sum = elements * (elements + 1) // 2
        repeating: int = 0
        total = 0
        for row in range(n):
            for col in range(n):
                num = abs(grid[row][col])
                index = num - 1
                r, c = index // n, index % n
                if grid[r][c] < 0:
                    repeating = num
                else:
                    grid[r][c] *= -1
                    total += num

        return [repeating, expected_sum - total]

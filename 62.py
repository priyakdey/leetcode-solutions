from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr_row: List[int] = [1] * n
        prev_row: List[int] = [1] * n

        for row in range(m - 1):
            for col in range(n - 2, -1, -1):
                curr_row[col] = curr_row[col + 1] + prev_row[col]

            # copy curr_row into prev_row
            prev_row[:] = curr_row

        return curr_row[0]

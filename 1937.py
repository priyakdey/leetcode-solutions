"""
You are given an m x n integer matrix points (0-indexed). Starting with 0
points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at
coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you
picked in the previous row. For every two adjacent rows r and r + 1
(where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2)
will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
"""

from typing import List, Optional


INT_MAX = (1 << 31) - 1
INT_MIN = -(1 << 31)


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])

        max_points: List[List[int]] = [[0 for _ in range(cols)] for _ in range(rows)]
        for col in range(cols):
            max_points[0][col] = points[0][col]

        for row in range(1, rows):
            for col in range(cols):
                point = INT_MIN
                for prev_col in range(cols):
                    point = max(point, points[row][col] + max_points[row - 1][prev_col] - abs(col - prev_col))
                max_points[row][col] = point

        return max(max_points[-1])


    def _maxPoints(self, points: List[List[int]]) -> int:
        def collect_points(
            row: int, prev_col: int, cache: List[List[Optional[int]]]
        ) -> int:
            nonlocal rows, cols

            if row == rows:
                return 0

            if prev_col != -1 and cache[row][prev_col] is not None:
                return cache[row][prev_col]

            point = INT_MIN
            for curr_col in range(cols):
                _point = points[row][curr_col] + collect_points(
                    row + 1, curr_col, cache
                )
                if prev_col != -1:
                    _point = _point - abs(prev_col - curr_col)
                point = max(point, _point)

            cache[row][prev_col] = point
            return point

        rows, cols = len(points), len(points[0])
        cache: List[List[Optional[int]]] = [
            [None for _ in range(cols + 1)] for _ in range(rows + 1)
        ]
        return collect_points(0, -1, cache)

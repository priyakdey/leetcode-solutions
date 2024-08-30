"""
130. Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O', capture
regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.
- Region: To form a region connect every 'O' cell.
- Surround: The region is surrounded with 'X' cells if you can connect the
  region with 'X' cells and none of the region cells are on the edge of the
  board.

A surrounded region is captured by replacing all 'O's with 'X's in the input
matrix board.
"""

from collections import deque
from typing import Deque, List, Set, Tuple


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        queue: Deque[Tuple[int, int]] = deque()
        visited: Set[Tuple[int, int]] = set()
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for col in range(cols):
            if board[0][col] == "O":
                queue.append((0, col))
                visited.add((0, col))
            if board[rows - 1][col] == "O":
                queue.append((rows - 1, col))
                visited.add((rows - 1, col))

        for row in range(rows):
            if board[row][0] == "O":
                queue.append((row, 0))
                visited.add((row, 0))
            if board[row][cols - 1] == "O":
                queue.append((row, cols - 1))
                visited.add((row, cols - 1))

        while len(queue) > 0:
            row, col = queue.popleft()

            for dy, dx in directions:
                next_row = row + dy
                next_col = col + dx
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and board[next_row][next_col] == "O"
                    and (next_row, next_col) not in visited
                ):
                    queue.append((next_row, next_col))
                    visited.add((next_row, next_col))

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited:
                    board[row][col] = "X"

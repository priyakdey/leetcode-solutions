# https://leetcode.com/problems/game-of-life/description
from typing import List, Tuple


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def count_nbors(row: int, col: int) -> int:
            nonlocal board, rows, cols

            live = 0

            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    next_row, next_col = row + dr, col + dc
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        live += board[next_row][next_col]

            return live

        rows, cols = len(board), len(board[0])
        buffer: List[List[int]] = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1 and count_nbors(row, col) not in [2, 3]:
                    buffer[row][col] = 0
                elif board[row][col] == 0 and count_nbors(row, col) == 3:
                    buffer[row][col] = 1
                else:
                    buffer[row][col] = board[row][col]

        for row in range(rows):
            for col in range(cols):
                board[row][col] = buffer[row][col]

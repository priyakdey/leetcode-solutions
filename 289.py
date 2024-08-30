"""
289. Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway
in 1970."

The board is made up of an m x n grid of cells, where each cell has an
initial state: live (represented by a 1) or dead (represented by a 0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies as if caused by
  under-population.
- Any live cell with two or three live neighbors lives on to the next
  generation.
- Any live cell with more than three live neighbors dies, as if by
  over-population.
- Any dead cell with exactly three live neighbors becomes a live cell, as if
  by reproduction.

The next state is created by applying the above rules simultaneously to every
cell in the current state, where births and deaths occur simultaneously.
Given the current state of the m x n grid board, return the next state.
"""

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def count_live_nbors(row: int, col: int) -> int:
            nonlocal board, rows, cols

            live = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    if 0 <= row + dy < rows and 0 <= col + dx < cols:
                        live += board[row + dy][col + dx]

            return live

        rows, cols = len(board), len(board[0])
        back: List[List[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                live_count = count_live_nbors(row, col)
                if board[row][col] == 1 and 2 <= live_count <= 3:
                    back[row][col] = 1
                elif board[row][col] == 0 and live_count == 3:
                    back[row][col] = 1
                else:
                    back[row][col] = 0

        for row in range(rows):
            for col in range(cols):
                board[row][col] = back[row][col]

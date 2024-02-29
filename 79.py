"""
79. Word Search

Given an m x n grid of characters board and a string word, return true if 
word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if self._exist(board, row, col, word, 0):
                    return True

        return False

    def _exist(
        self,
        board: List[List[str]],
        row: int,
        col: int,
        word: str,
        index: int,
    ) -> bool:
        rows, cols = len(board), len(board[0])

        if index == len(word):
            return True
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        if board[row][col] != word[index]:
            return False

        ch = board[row][col]
        board[row][col] = "#"

        exists = (
            self._exist(board, row + 1, col, word, index + 1)
            or self._exist(board, row - 1, col, word, index + 1)
            or self._exist(board, row, col + 1, word, index + 1)
            or self._exist(board, row, col - 1, word, index + 1)
        )

        board[row][col] = ch
        return exists

"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 
  1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable. 
Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.validate_rows(board)
            and self.validate_cols(board)
            and self.validate_sub_grid(board)
        )

    def validate_rows(self, board: List[List[str]]) -> bool:
        for row in range(9):
            bitmap = 0
            for col in range(9):
                ch = board[row][col]
                if ch != ".":
                    digit = int(ch)
                    if (bitmap >> (digit - 1)) & 1 == 1:
                        return False
                    bitmap = bitmap | (1 << (digit - 1))

        return True

    def validate_cols(self, board: List[List[str]]) -> bool:
        for col in range(9):
            bitmap = 0
            for row in range(9):
                ch = board[row][col]
                if ch != ".":
                    digit = int(ch)
                    if (bitmap >> (digit - 1)) & 1 == 1:
                        return False
                    bitmap = bitmap | (1 << (digit - 1))

        return True

    def validate_sub_grid(self, board: List[List[str]]) -> bool:
        for row_range in range(0, 9, 3):
            for col_range in range(0, 9, 3):
                bitmap = 0
                for row in range(row_range, row_range + 3):
                    for col in range(col_range, col_range + 3):
                        ch = board[row][col]
                        if ch != ".":
                            digit = int(ch)
                            if (bitmap >> (digit - 1)) & 1 == 1:
                                return False
                            bitmap = bitmap | (1 << (digit - 1))

        return True

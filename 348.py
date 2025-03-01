from typing import List


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board: List[List[int]] = [[0 for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        count = 0
        for c in range(self.n):
            if self.board[row][c] == player:
                count += 1

        if count == self.n:
            return player

        count = 0
        for r in range(self.n):
            if self.board[r][col] == player:
                count += 1

        if count == self.n:
            return player

        count = 0
        for r in range(self.n):
            if self.board[r][r] == player:
                count += 1

        if count == self.n:
            return player

        count = 0
        for r in range(self.n):
            if self.board[r][self.n - r - 1] == player:
                count += 1

        if count == self.n:
            return player

        return 0

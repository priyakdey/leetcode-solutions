"""
Assume the following rules are for the tic-tac-toe game on an n x n board 
between two players:

- A move is guaranteed to be valid and is placed on an empty block.
- Once a winning condition is reached, no more moves are allowed.
- A player who succeeds in placing n of their marks in a horizontal, vertical, 
  or diagonal row wins the game.

Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
- int move(int row, int col, int player) Indicates that the player with id 
  player plays at the cell (row, col) of the board. The move is guaranteed to 
  be a valid move, and the two players alternate in making moves. Return
    - 0 if there is no winner after the move,
    - 1 if player 1 is the winner after the move, or
    - 2 if player 2 is the winner after the move.
"""


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range((n))]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if self.did_win(row, col, player):
            return player

    def did_win(self, row: int, col: int, player: int) -> bool:
        win = True

        if row + col == self.n - 1:
            # check forward diagonal
            r, c = row, col
            while r + 1 < self.n and c + 1 < self.n:
                r = r + 1
                c = c + 1
                if self.board[r][c] != player:
                    win = False
                    break
            r, c = row, col
            while r - 1 >= 0 and c - 1 >= 0:
                r = r - 1
                c = c - 1
                if self.board[r][c] != player:
                    win = False
                    break

            if win:
                return True

            # check backward diagonal
            r, c = row, col
            while r + 1 < self.n and c - 1 >= 0:
                r = r + 1
                c = c - 1
                if self.board[r][c] != player:
                    win = False
                    break
            r, c = row, col
            while r - 1 >= 0 and c + 1 < self.n:
                r = r - 1
                c = c + 1
                if self.board[r][c] != player:
                    win = False
                    break

            if win:
                return True

        # check row
        c = col
        while c < self.n:
            if self.board[row][c] != player:
                win = False
                break
            c += 1
        c = col
        while c >= 0:
            if self.board[row][c] != player:
                win = False
                break
            c -= 1

        if win:
            return True

        # check col
        r = row
        while r < self.n:
            if self.board[r][col] != player:
                win = False
                break
            r += 1
        r = row
        while r >= 0:
            if self.board[r][col] != player:
                win = False
                break
            r -= 1

        return win


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

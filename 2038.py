"""
2038. Remove Colored Pieces if Both Neighbors are the Same Color

There are n pieces arranged in a line, and each piece is colored either by 'A' 
or by 'B'. You are given a string colors of length n where colors[i] is the 
color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing 
pieces from the line. In this game, Alice moves first.

- Alice is only allowed to remove a piece colored 'A' if both its neighbors are 
  also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
- Bob is only allowed to remove a piece colored 'B' if both its neighbors are 
  also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
- Alice and Bob cannot remove pieces from the edge of the line.
- If a player cannot make a move on their turn, that player loses and the other 
  player wins.

Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        total_moves_alice = self.calc_total_moves(colors, "A")
        total_moves_bob = self.calc_total_moves(colors, "B")

        if total_moves_alice == 0:
            return False
        return total_moves_alice > total_moves_bob

    def calc_total_moves(self, colors: str, color: str) -> int:
        total_moves = 0
        cursor = 0
        length = len(colors)
        while cursor < length:
            if colors[cursor] == color:
                start = cursor
                while cursor < length and colors[cursor] == color:
                    cursor += 1

                moves = (cursor - 1) - start + 1 - 2
                if moves > 0:
                    total_moves += moves

            cursor += 1

        return total_moves

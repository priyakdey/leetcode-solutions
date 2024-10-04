"""
293. Flip Game


You are given a string currentState that contains only '+' and '-'. You and
your friend take turns to flip two consecutive "++" into "--". The game ends
when a person can no longer make a move, and therefore the other person will
be the winner.

Return all possible states of the string currentState after one valid move.
You may return the answer in any order. If there is no valid move,
return an empty list [].
"""
from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if len(currentState) < 2:
            return []

        buf: List[str] = list(currentState)
        output: List[str] = []

        for i in range(1, len(buf)):
            if buf[i] == buf[i - 1] and buf[i] == "+":
                buf[i] = "-"
                buf[i - 1] = "-"
                output.append("".join(buf))
                buf[i] = "+"
                buf[i - 1] = "+"

        return output



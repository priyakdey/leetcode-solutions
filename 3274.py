"""
3274. Check if Two Chessboard Squares Have the Same Color

You are given two strings, coordinate1 and coordinate2, representing the
coordinates of a square on an 8 x 8 chessboard.

Below is the chessboard for reference.
"""


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def to_color(cell: str) -> str:
            x = ord(cell[0]) - 97
            y = int(cell[1])

            if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
                return "black"
            else:
                return "white"

        return to_color(coordinate1) == to_color(coordinate2)

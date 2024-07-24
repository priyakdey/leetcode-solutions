"""
3200. Maximum Height of a Triangle

You are given two integers red and blue representing the count of red and
blue colored balls. You have to arrange these balls to form a triangle such
that the 1st row will have 1 ball, the 2nd row will have 2 balls, the 3rd row
will have 3 balls, and so on.

All the balls in a particular row should be the same color, and adjacent rows
should have different colors.

Return the maximum height of the triangle that can be achieved.
"""


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.height(red, blue, "red"), self.height(red, blue, "blue"))

    @staticmethod
    def height(red: int, blue: int, current_color: str) -> int:
        height = 0

        while True:
            if current_color == "red":
                if red >= height + 1:
                    red -= height + 1
                else:
                    break
            else:
                if blue >= height + 1:
                    blue -= height + 1
                else:
                    break

            height += 1
            current_color = "blue" if current_color == "red" else "red"

        return height

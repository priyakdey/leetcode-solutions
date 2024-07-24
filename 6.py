"""
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a
number of rows:

string convert(string s, int numRows);
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        going_down = True

        for ch in s:
            rows[row] += ch
            if row == 0:
                going_down = True
            elif row == numRows - 1:
                going_down = False

            row = row + 1 if going_down else row - 1

        return "".join(rows)

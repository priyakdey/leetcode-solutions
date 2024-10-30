"""
2938. Separate Black and White Balls

There are n balls on a table, each ball has a color black or white.

You are given a 0-indexed binary string s of length n, where 1 and 0 represent
black and white balls, respectively.

In each step, you can choose two adjacent balls and swap them.

Return the minimum number of steps to group all the black balls to the right
and all the white balls to the left.
"""

class Solution:
    def minimumSteps(self, s: str) -> int:
        left, right = 0, len(s) - 1
        swaps = 0

        while left < right:
            if s[left] == "0" and s[right] == "0":
                left += 1
            elif s[left] == "0" and s[right] == "1":
                left += 1
                right -= 1
            elif s[left] == "1" and s[right] == "0":
                swaps += right - left
                left += 1
                right -= 1
            else:
                right -= 1

        return swaps

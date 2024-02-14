"""
796. Rotate String

Given two strings s and goal, return true if and only if s can become goal 
after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost 
position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return True

        for i in range(1, len(s)):
            if s[:i] == goal[len(goal) - i :] and s[i:] == goal[: len(goal) - i :]:
                return True

        return False

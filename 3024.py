"""
3024. Type of Triangle

You are given a 0-indexed integer array nums of size 3 which can form the
sides of a triangle.

- A triangle is called equilateral if it has all sides of equal length.
- A triangle is called isosceles if it has exactly two sides of equal length.
- A triangle is called scalene if all its sides are of different lengths.

Return a string representing the type of triangle that can be formed or "none"
if it cannot form a triangle.
"""

from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        x, y, z = nums[0], nums[1], nums[2]

        if x + y <= z or x + z <= y or y + z <= x:
            return "none"

        if x == y == z:
            return "equilateral"
        elif x == y or y == z or x == z:
            return "isosceles"
        else:
            return "scalene"

"""
407. Trapping Rain Water II

Given an m x n integer matrix heightMap representing the height of each unit
cell in a 2D elevation map, return the volume of water it can trap after
raining.
"""
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])

        left_height: List[int]  = [0] * rows
        right_height: List[int] = [0] * rows
        top_height: List[int]   = [0] * cols
        down_height: List[int]  = [0] * cols


        for row in range(1, rows):
            right_height[row] = heightMap[row - 1][0]


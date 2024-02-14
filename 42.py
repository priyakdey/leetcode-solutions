"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it can trap after raining.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length <= 2:
            return 0

        max_height = height[0]
        left_bound_height: List[int] = [0 for _ in range(length)]
        for i in range(1, length):
            max_height = max(max_height, height[i - 1])
            left_bound_height[i] = max_height

        max_height = height[-1]
        right_bound_height: List[int] = [0 for _ in range(length)]
        for i in range(length - 2, -1, -1):
            max_height = max(max_height, height[i + 1])
            right_bound_height[i] = max_height

        total_area = 0
        for i in range(1, length - 1):
            bound_height = min(left_bound_height[i], right_bound_height[i])
            if bound_height > height[i]:
                total_area += (bound_height - height[i]) * 1

        return total_area

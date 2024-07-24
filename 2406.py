"""
2406. Divide Intervals Into Minimum Number of Groups

You are given a 2D integer array intervals where intervals[i] = [lefti, righti]
represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each
interval is in exactly one group, and no two intervals that are in the same
group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them.
For example, the intervals [1, 5] and [5, 8] intersect.
"""

from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))

        groups: List[List[int]] = [intervals[0]]
        # print(intervals)

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            left, right = 0, len(groups) - 1
            index = -1
            while left <= right:
                mid = left + (right - left) // 2
                if start >= groups[mid][1]:
                    index = mid
                    left = mid + 1
                else:
                    right = mid - 1

            if index == -1:
                groups.append([start, end])
            else:
                groups[index][1] = end

        # print(groups)

        return len(groups)

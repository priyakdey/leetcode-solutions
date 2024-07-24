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
        print(intervals)
        groups = 0

        for i in range(len(intervals)):
            if intervals[i][0] < 0:
                continue

            intervals[i][0] *= 1
            last_end_time = intervals[i][1]
            for j in range(len(intervals)):
                start_time, end_time = intervals[j]
                if start_time < 0:
                    continue
                if start_time > last_end_time:
                    intervals[j][0] *= -1
                    last_end_time = intervals[j][1]

            groups += 1

        return groups

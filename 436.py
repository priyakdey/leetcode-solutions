"""
436. Find Right Interval

You are given an array of intervals, where intervals[i] = [starti, endi] and 
each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi 
and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. 
If no right interval exists for interval i, then put -1 at index i.
"""

from typing import Dict, List, Tuple


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index_map: Dict[Tuple[int, int], int] = {}
        for index, [start, end] in enumerate(intervals):
            index_map[(start, end)] = index

        print(index_map)

        sorted_intervals = sorted([(start, end) for [start, end] in intervals])

        result = [-1] * len(intervals)

        for index, [_, end] in enumerate(intervals):
            left, right = 0, len(sorted_intervals) - 1
            right_interval_index = -1
            while left <= right:
                mid = left + (right - left) // 2
                if sorted_intervals[mid][0] >= end:
                    right_interval_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if right_interval_index != -1:
                result[index] = index_map[sorted_intervals[right_interval_index]]

        return result

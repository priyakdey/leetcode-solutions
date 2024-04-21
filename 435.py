"""
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of 
the intervals non-overlapping.
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])

        count = 0
        last_end_time = intervals[0][1]

        for i in range(1, len(intervals)):
            curr_start_time, curr_end_time = intervals[i][0], intervals[i][1]

            if curr_start_time >= last_end_time:
                # non overlapping interval. keep the interval and change last_end_time
                last_end_time = curr_end_time
            else:
                # overlapping interval, skip over
                count += 1

        return count

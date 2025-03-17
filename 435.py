from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        remove = 0

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if curr_start < prev_end:
                remove += 1
            else:
                prev_end = curr_end

        return remove

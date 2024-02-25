"""
57. Insert Interval

You are given an array of non-overlapping intervals intervals where 
intervals[i] = [starti, endi] represent the start and the end of the ith 
interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the 
start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any overlapping 
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        # Step 1: Binary Search to find insertion position
        left, right = 0, len(intervals) - 1

        insert_at = None
        while left <= right:
            mid = left + (right - left) // 2
            if newInterval[0] == intervals[mid][0]:
                intervals.insert(mid, newInterval)
                break
            if newInterval[0] < intervals[mid][0]:
                if mid == 0:
                    intervals.insert(mid, newInterval)
                    break
                if newInterval[0] > intervals[mid - 1][0]:
                    intervals.insert(mid, newInterval)
                    break
                else:
                    right = mid - 1
            else:
                if mid == len(intervals) - 1:
                    intervals.append(newInterval)
                    break
                if newInterval[0] < intervals[mid + 1][0]:
                    intervals.insert(mid + 1, newInterval)
                    break
                else:
                    left = mid + 1

        # Step 2: Merge the intervals
        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] == merged_intervals[-1][0]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])
            elif intervals[i][0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])
            else:
                if intervals[i][1] >= merged_intervals[-1][1]:
                    merged_intervals.append(intervals[i])
                else:
                    merged_intervals[-1][0] = min(
                        merged_intervals[-1][0], intervals[i][0]
                    )
                    merged_intervals[-1][1] = max(
                        merged_intervals[-1][1], intervals[i][1]
                    )

        return merged_intervals

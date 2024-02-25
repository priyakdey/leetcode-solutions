"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sort(intervals):
            partition(intervals, 0, len(intervals) - 1)
            return intervals

        def partition(intervals, start, end) -> None:
            if start >= end:
                return
            mid = start + (end - start) // 2
            partition(intervals, start, mid)
            partition(intervals, mid + 1, end)
            merge(intervals, start, mid, end)

        def merge(intervals, start, mid, end):
            merged = []
            iter1, iter2 = start, mid + 1

            while iter1 <= mid and iter2 <= end:
                if intervals[iter1][0] < intervals[iter2][0]:
                    merged.append(intervals[iter1])
                    iter1 += 1
                elif intervals[iter1][0] > intervals[iter2][0]:
                    merged.append(intervals[iter2])
                    iter2 += 1
                else:
                    if intervals[iter1][1] <= intervals[iter2][1]:
                        merged.append(intervals[iter1])
                        iter1 += 1
                    else:
                        merged.append(intervals[iter2])
                        iter2 += 1

            while iter1 <= mid:
                merged.append(intervals[iter1])
                iter1 += 1

            while iter2 <= mid:
                merged.append(intervals[iter2])
                iter2 += 1

            curr = start
            for interval in merged:
                intervals[curr] = interval
                curr += 1

        # sort the intervals
        intervals = sort(intervals)

        # now merge
        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_start, curr_start = merged_intervals[-1][0], intervals[i][0]
            prev_end, curr_end = merged_intervals[-1][1], intervals[i][1]

            start, end = curr_start, curr_end

            if curr_start <= prev_start:
                start = curr_start
                end = max(prev_end, curr_end)
                merged_intervals.pop(-1)
            else:
                if curr_start <= prev_end:
                    start = prev_start
                    end = max(prev_end, curr_end)
                    merged_intervals.pop(-1)
            merged_intervals.append([start, end])

        return merged_intervals

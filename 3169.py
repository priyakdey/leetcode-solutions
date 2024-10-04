"""
3169. Count Days Without Meetings

You are given a positive integer days representing the total number of days an
employee is available for work (starting from day 1). You are also given a 2D
array meetings of size n where, meetings[i] = [start_i, end_i] represents the
starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no
meetings are scheduled.

Note: The meetings may overlap.
"""
from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: (x[0], x[1]))
        merged: List[List[int]] = [meetings[0]]

        for i in range(1, len(meetings)):
            curr_start = meetings[i][0]
            curr_end = meetings[i][1]

            prev_start = merged[-1][0]
            prev_end = merged[-1][1]

            if curr_start <= prev_end:
                merged[-1][0] = prev_start
                merged[-1][0] = max(prev_end, curr_end)
            else:
                merged.append([curr_start, curr_end])


        last_end: int = 0
        count: int = 0
        for start, end in merged:
            if start > last_end:
                count += 1
            last_end = end

        if 10 > last_end:
            count += 1

        return count

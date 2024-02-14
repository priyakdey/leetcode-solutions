"""
253. Meeting Rooms II

Given an array of meeting time intervals intervals where 
intervals[i] = [starti, endi], return the minimum number of conference rooms required.
"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = [interval[0] for interval in intervals]
        end_times = [interval[1] for interval in intervals]
        start_times.sort()
        end_times.sort()

        min_rooms = 1
        empty_rooms = 0
        i, j = 1, 0

        while i < len(start_times):
            if start_times[i] < end_times[j]:
                if empty_rooms == 0:
                    min_rooms += 1
                else:
                    empty_rooms -= 1
                i += 1
            else:
                empty_rooms += 1
                j += 1

        return min_rooms

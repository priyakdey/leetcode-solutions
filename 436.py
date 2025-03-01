from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def index_of(interval: List[int]) -> int:
            nonlocal sorted_intervals

            index = -1
            left, right = 0, len(sorted_intervals) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if sorted_intervals[mid][0] >= interval[1]:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return sorted_intervals[index][2] if index != -1 else -1

        sorted_intervals = [
            [start, end, index] for index, [start, end] in enumerate(intervals)
        ]
        sorted_intervals.sort(key=lambda x: (x[0], x[1]))
        result: List[int] = [-1] * len(intervals)

        for i, interval in enumerate(intervals):
            result[i] = index_of(interval)

        return result

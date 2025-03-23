from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        arrows = 1
        prev_start, prev_end = points[0][0], points[0][1]

        for i in range(1, len(points)):
            curr_start, curr_end = points[i][0], points[i][1]

            if curr_start <= prev_end:
                prev_start = max(prev_start, curr_start)
                prev_end = min(prev_end, curr_end)
            else:
                prev_start, prev_end = curr_start, curr_end
                arrows += 1

        return arrows

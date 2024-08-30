"""
452. Minimum Number of Arrows to Burst Balloons

There are some spherical balloons taped onto a flat wall that represents the 
XY-plane. The balloons are represented as a 2D integer array points where 
points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches 
between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from 
different points along the x-axis. A balloon with xstart and xend is burst by 
an arrow shot at x if xstart <= x <= xend. 
There is no limit to the number of arrows that can be shot. 
A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot 
to burst all balloons.
"""

from typing import List


class Solution:
    class Solution:
        def findMinArrowShots(self, points: List[List[int]]) -> int:
            points.sort(key=lambda x: (x[0], x[1]))

            prev_start = points[0][0]
            prev_end = points[0][1]
            arrows = 1

            for i in range(1, len(points)):
                curr_start = points[i][0]
                curr_end = points[i][1]

                if curr_start <= prev_end:
                    prev_start = max(curr_start, prev_start)
                    prev_end = min(curr_end, prev_end)
                else:
                    prev_start = curr_start
                    prev_end = curr_end
                    arrows += 1

            return arrows

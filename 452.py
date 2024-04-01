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
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        points.sort(key=lambda arr: (arr[0], arr[1]))
        return self.fake_merge(points)

    def fake_merge(self, points: List[List[int]]) -> int:
        """Does not actually merge, but returns the count of total interval
        if merge of overlapping positions did happen"""
        count = 1
        cursor = 0

        prevStart = points[cursor][0]
        prevEnd = points[cursor][1]

        for i in range(1, len(points)):
            currStart = points[i][0]
            currEnd = points[i][1]

            if currStart == prevStart or currStart <= prevEnd:
                prevStart = prevStart
                prevEnd = min(prevEnd, currEnd)
                continue
            else:
                prevStart = currStart
                prevEnd = currEnd
                cursor += 1
                count += 1

        return count

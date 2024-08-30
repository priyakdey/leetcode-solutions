"""
149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane, return the maximum number of points that lie on the same straight
line.
"""

from collections import defaultdict
from typing import Dict, List, Set, Tuple


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def calc_slope(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
            """Calculate the slope of a line given two points."""
            if point1[0] == point2[0]:
                return float("inf")

            return (point1[1] - point2[1]) / (point1[0] - point2[0])

        def calc_intercept(point: Tuple[int, int], slope: float) -> float:
            """Calculate the intercept of a line given one point and a slope"""
            if slope == float("inf"):
                return point[0]

            return point[1] - (slope * point[0])

        if points is None or len(points) == 0:
            raise Exception("Empty array")
        if len(points) < 3:
            return len(points)

        line_equations: Dict[Tuple[float, float], Set[Tuple[int, int]]] = defaultdict(
            set
        )

        for i in range(len(points) - 1):
            point1: Tuple[int, int] = (points[i][0], points[i][1])
            for j in range(i + 1, len(points)):
                point2: Tuple[int, int] = (points[j][0], points[j][1])
                slope = calc_slope(point1, point2)
                intercept = calc_intercept(point1, slope)
                key = (slope, intercept)
                line_equations[key].add(point1)
                line_equations[key].add(point2)

        max_points = 0
        for _, points in line_equations.items():
            if len(points) > max_points:
                max_points = len(points)

        return max_points

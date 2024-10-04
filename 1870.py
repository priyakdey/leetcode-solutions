"""
1870. Minimum Speed to Arrive on Time

You are given a floating-point number hour, representing the amount of time
you have to reach the office. To commute to the office, you must take n trains
in sequential order. You are also given an integer array dist of length n,
where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in
between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an
additional 0.5 hours before you can depart on the 2nd train ride at the
2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all
the trains must travel at for you to reach the office on time, or -1 if it is
impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have
at most two digits after the decimal point.
"""
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def calc_total_time(speed: int, distances: List[int]) -> int:
            total_time = 0

            for i, distance in enumerate(distances):
                if i < len(distances) - 1:
                    total_time += distance // speed
                    total_time += 1 if distance % speed != 0 else -1
                else:
                    total_time += distance // speed

            return total_time

        min_speed, max_speed = 1, max(dist)
        speed = -1

        while min_speed <= max_speed:
            min_speed = min_speed + (max_speed - min_speed) // 2
            time = calc_total_time(min_speed, dist)
            if time <= hour:
                speed = min_speed
                max_speed = min_speed - 1
            else:
                min_speed = min_speed + 1

        return speed



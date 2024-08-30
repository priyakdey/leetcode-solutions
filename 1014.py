"""
1014. Best Sightseeing Pair

You are given an integer array values where values[i] represents the value of
the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i
between them.

The score of a pair (i < j) of sightseeing spots is
values[i] + values[j] + i - j: the sum of the values of the sightseeing spots,
minus the distance between them.

Return the maximum score of a pair of sightseeing spots.
"""

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        if values is None or len(values) < 2:
            raise Exception("invalid argument")

        max_value, max_index = values[0], 0
        max_score = 0
        for i in range(1, len(values)):
            value = values[i]
            max_score = max(max_score, value + max_value - (i - max_index))
            if value >= max_value:
                max_value = value
                max_index = i

        return max_score

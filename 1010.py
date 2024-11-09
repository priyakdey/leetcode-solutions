"""
1010. Pairs of Songs With Total Durations Divisible by 60


You are given a list of songs where the ith song has a duration of time[i]
seconds.

Return the number of pairs of songs for which their total duration in seconds
is divisible by 60. Formally, we want the number of indices i, j such that
i < j with (time[i] + time[j]) % 60 == 0.
"""
from collections import defaultdict
from typing import Dict, List


class Solution:
    def numPairsDivisibleBy60(self, times: List[int]) -> int:
        foo: Dict[int, int] = defaultdict(int)
        total_pairs: int = 0

        for time in times:
            x = time % 60
            y = 60 - x
            if y in foo:
                total_pairs += foo[y]

            foo[x] += 1

        return total_pairs


from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_distance = 0

        for i in range(len(arrays)):
            for j in range(len(arrays)):
                if i == j:
                    continue
                max_distance = max(max_distance, abs(arrays[j][-1] - arrays[i][0]))

        return max_distance

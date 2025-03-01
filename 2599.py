from heapq import heappush, heappop
from typing import List


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        heap: List[int] = []

        prefix_sum = 0

        for num in nums:
            heappush(heap, num)
            if prefix_sum + num >= 0:
                prefix_sum += num
            else:
                heappop(heap)
                count += 1

        return count

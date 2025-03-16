from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = 0
        total_sum = 0

        for i in range(k):
            total_sum += nums[i]

        max_avg = total_sum / k

        for i in range(k, len(nums)):
            total_sum = total_sum + nums[i] - nums[i - k]
            avg = total_sum / k
            max_avg = max(max_avg, avg)

        return max_avg

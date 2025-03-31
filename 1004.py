from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_length = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1

            if k == -1:
                max_length = max(max_length, i - start)
                while nums[start] != 0:
                    start += 1
                start += 1
                k += 1

        max_length = max(max_length, len(nums) - start)
        return max_length

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start, curr = 0, 0
        removed = 0
        max_length = 0
        while curr < len(nums):
            if nums[curr] == 0:
                if removed == 1:
                    max_length = max(max_length, curr - start)
                    while removed > 1:
                        if nums[start] == 0:
                            removed -= 1
                        start += 1
                else:
                    removed = 1
            curr += 1

        max_length = max(max_length, curr - start)
        return max_length

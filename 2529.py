from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # find rightmost -ve number
        length = len(nums)
        left, right = 0, length - 1
        negative_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                negative_index = mid
                left = mid + 1
            else:
                right = mid - 1

        negative_count = negative_index - 0 + 1

        # find leftmost +ve number
        left, right = 0, length - 1
        positive_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                positive_index = mid
                right = mid - 1
            else:
                left = mid + 1

        positive_count = length - 1 - positive_index + 1 if positive_index != -1 else 0

        return max(positive_count, negative_count)

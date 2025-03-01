from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        assert nums is not None and len(nums) > 0
        min_element = nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left)
            if nums[mid] <= nums[-1]:
                min_element = min(min_element, nums[mid])
                right = mid - 1
            else:
                left = mid + 1

        return min_element

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            raise Exception("invalid input")

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])

        left, right = 0, len(nums) - 1
        min_element = (1 << 31) - 1

        while left <= right:
            mid = left + (right - left) // 2

            while left <= right and nums[left] == nums[mid]:
                min_element = min(min_element, nums[mid])
                left += 1
                continue

            if nums[right] == nums[mid]:
                min_element = min(min_element, nums[mid])
                right -= 1
                continue

            if nums[mid] < nums[right]:
                min_element = min(min_element, nums[mid])
                right = mid - 1
            else:
                left = mid + 1

        return min_element

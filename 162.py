from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return length - 1

        left, right = 1, length - 2
        index = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                index = mid
                break
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return index

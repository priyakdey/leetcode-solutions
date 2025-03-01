# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                index = mid
                break
            if target > nums[mid]:
                if nums[mid] > nums[-1]:
                    left = mid + 1
                else:
                    if target <= nums[-1]:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                if nums[mid] > nums[-1]:
                    if target <= nums[-1]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    right = mid - 1

        return index

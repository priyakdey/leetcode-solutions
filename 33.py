"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                index = mid
                break

            if nums[mid] <= nums[-1]:
                # mid is in the right sorted half
                if target < nums[mid]:
                    right = mid - 1
                else:
                    if target <= nums[-1]:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                if target < nums[mid]:
                    if target >= nums[0]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    left = mid + 1

        return index

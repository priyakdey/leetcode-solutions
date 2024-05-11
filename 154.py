"""
154. Find Minimum in Rotated Sorted Array II

Suppose an array of length n sorted in ascending order is rotated between 1 and 
n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

- [4,5,6,7,0,1,4] if it was rotated 4 times.
- [0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in 
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, 
return the minimum element of this array.

You must decrease the overall operation steps as much as possible.
"""

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

            if nums[left] == nums[mid]:
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

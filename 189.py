"""
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, 
where k is non-negative.
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverseInRange(arr: List[int], start: int, end: int) -> None:
            """Reverses the array in the given range - [start, end]"""
            while start < end:
                temp = arr[start]
                arr[start] = arr[end]
                arr[end] = temp
                start += 1
                end -= 1

        k = k % len(nums)
        if k != 0:
            # reverse the whole array
            reverseInRange(nums, 0, len(nums) - 1)
            # reverse the first k elements
            reverseInRange(nums, 0, k - 1)
            # reverse the last elements from k
            reverseInRange(nums, k, len(nums) - 1)

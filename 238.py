"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
integer.

You must write an algorithm that runs in O(n) time and without using the 
division operation.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1 for _ in nums]

        prefix_product, suffix_product = 1, 1
        left, right = 1, len(nums) - 2

        while left < len(nums):
            prefix_product *= nums[left - 1]
            product[left] *= prefix_product
            left += 1

            suffix_product *= nums[right + 1]
            product[right] *= suffix_product
            right -= 1

        return product

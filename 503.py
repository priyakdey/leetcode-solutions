"""
503. Next Greater Element II

Given a circular integer array nums (i.e., the next element of
nums[nums.length - 1] is nums[0]), return the next greater number for every
element in nums.

The next greater number of a number x is the first greater number to its
traversing-order next in the array, which means you could search circularly
to find its next greater number. If it doesn't exist, return -1 for this number.
"""

from collections import deque
from typing import List, Deque, Tuple


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack: Deque[Tuple[int, int]] = deque()

        next_greater_element = [-1] * len(nums)

        for index, num in enumerate(nums):
            while len(stack) > 0 and num > stack[-1][0]:
                _, i = stack.pop()
                next_greater_element[i] = num
            stack.append((num, index))

        for index, num in enumerate(nums):
            while len(stack) > 0 and num > stack[-1][0]:
                _, i = stack.pop()
                next_greater_element[i] = num
            stack.append((num, index))

        return next_greater_element

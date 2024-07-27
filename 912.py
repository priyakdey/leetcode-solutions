"""
912. Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n))
time complexity and with the smallest space complexity possible.
"""

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        for i in range((len(nums) - 2) // 2, -1, -1):
            Solution.heapify(nums, i, len(nums))

        for i in range(len(nums) - 1, -1, -1):
            Solution.swap(nums, 0, i)
            Solution.heapify(nums, 0, i)

        return nums

    @staticmethod
    def swap(nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    @staticmethod
    def heapify(nums: List[int], root_index: int, length: int) -> None:
        swap_index = root_index

        left_child  = 2 * root_index + 1
        right_child = 2 * root_index + 2

        if left_child < length and nums[left_child] > nums[swap_index]:
            swap_index = left_child

        if right_child < length and nums[right_child] > nums[swap_index]:
            swap_index = right_child

        if swap_index != root_index:
            Solution.swap(nums, swap_index, root_index)
            Solution.heapify(nums, swap_index, length)

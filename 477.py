"""
477. Total Hamming Distance

The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all
the pairs of the integers in nums.
"""
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        def calc_hamming_distance(num1: int, num2: int) -> int:
            distance = 0
            for i in range(32):
                distance += (num1 & 1) ^ (num2 & 1)
                num1 = num1 >> 1~
                num2 = num2 >> 1
            return distance

        total_distance = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                distance = calc_hamming_distance(nums[i], nums[j])
                total_distance += distance

        return total_distance
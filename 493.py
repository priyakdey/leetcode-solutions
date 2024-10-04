"""
493. Reverse Pairs

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

- 0 <= i < j < nums.length and
- nums[i] > 2 * nums[j].
"""

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.sort(nums, 0, len(nums) - 1)

    def sort(self, nums: List[int], left: int, right: int) -> int:
        if left >= right:
            return 0
        mid = left + (right - left) // 2
        return (
            self.sort(nums, left, mid)
            + self.sort(nums, mid + 1, right)
            + self.merge(nums, left, mid, mid + 1, right)
        )

    def merge(
        self,
        nums: List[int],
        left_start: int,
        left_end: int,
        right_start: int,
        right_end: int,
    ) -> int:
        len1 = left_end - left_start + 1
        len2 = right_end - right_start + 1
        length = len1 + len2
        merged: List[int] = [0] * length

        i, j = left_start, right_start
        curr = 0
        reverse_count: int = 0
        while i <= left_end and j <= right_end:
            if nums[i] > 2 * nums[j]:
                reverse_count += right_end - j + 1
            if nums[i] <= nums[j]:
                merged[curr] = nums[i]
                i += 1
            else:
                merged[curr] = nums[j]
                j += 1
            curr += 1

        while i <= left_end:
            merged[curr] = nums[i]
            i += 1
            curr += 1

        while j <= right_end:
            merged[curr] = nums[j]
            j += 1
            curr += 1

        curr = 0
        for i in range(left_start, left_end + 1):
            nums[i] = merged[curr]
            curr += 1
        for i in range(right_start, right_end + 1):
            nums[i] = merged[curr]
            curr += 1

        return reverse_count

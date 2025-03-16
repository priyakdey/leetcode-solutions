from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_at, curr = 0, 0

        while curr < len(nums):
            if nums[curr] != 0:
                nums[insert_at] = nums[curr]
                insert_at += 1
            curr += 1

        while insert_at < len(nums):
            nums[insert_at] = 0
            insert_at += 1

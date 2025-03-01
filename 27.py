# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr, swap = 0, 0
        while curr < len(nums):
            if nums[curr] != val:
                nums[swap] = nums[curr]
                swap += 1
            curr += 1

        return swap

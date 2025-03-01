from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] << 1
                nums[i + 1] = 0
        
        attach = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[attach] = nums[i]
                attach += 1
        
        for i in range(attach, len(nums)):
            nums[i] = 0
        
        return nums

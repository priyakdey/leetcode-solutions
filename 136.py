from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = 0
        for num in nums:
            number = number ^ num

        return number

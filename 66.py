"""
66. Plus One

You are given a large integer represented as an integer array digits, where 
each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in 
left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = [digit for digit in digits]
        carry = 1

        for i in range(len(sum) - 1, -1, -1):
            sum[i] = sum[i] + carry
            carry = sum[i] // 10
            sum[i] = sum[i] % 10

        if carry == 1:
            sum.insert(0, 1)

        return sum

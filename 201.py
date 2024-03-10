"""
201. Bitwise AND of Numbers Range

Given two integers left and right that represent the range [left, right], 
return the bitwise AND of all numbers in this range, inclusive.
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        for i in range(32):
            bit = 1
            for n in range(left, right + 1):
                if ((n >> i) & 1) == 0:
                    bit = 0
                    break
            result = result | (bit << i)

        return result

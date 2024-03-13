"""
791. Custom Sort String

You are given two strings order and s. All the characters of order are unique 
and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. 
More specifically, if a character x occurs before a character y in order, 
then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
"""

from typing import List


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        countArr: List[int] = [0 for _ in range(26)]
        for ch in s:
            countArr[ord(ch) - 97] += 1

        buffer: List[str] = []
        for ch in order:
            index = ord(ch) - 97
            buffer.append(ch * countArr[index])
            countArr[index] = 0

        for index, count in enumerate(countArr):
            if count == 0:
                continue

            ch = chr(index + 97)
            buffer.append(ch * count)

        return "".join(buffer)

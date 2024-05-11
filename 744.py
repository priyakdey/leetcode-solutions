"""
744. Find Smallest Letter Greater Than Target

You are given an array of characters letters that is sorted in non-decreasing 
order, and a character target. There are at least two different characters in 
letters.

Return the smallest character in letters that is lexicographically greater than 
target. If such a character does not exist, return the first character in letters.
"""

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if ord(letters[mid]) > ord(target):
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return letters[index] if index != -1 else letters[0]

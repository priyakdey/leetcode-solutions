"""
1291. Sequential Digits

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
"""

from typing import List, Tuple


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        start_num, start, digits, diff = self.find_start(low)
        sequence: List[int] = []

        curr = start_num

        while curr <= high:
            sequence.append(curr)
            if curr % 10 == 9:
                digits += 1
                curr = start * 10 + digits
                start = curr
                diff = diff * 10 + 1
            else:
                curr = curr + diff

        return sequence

    def find_start(self, low: int) -> Tuple[int, int, int, int]:
        start = 12
        curr = 12
        diff = 11
        digits = 2

        while curr < low:
            if curr % 10 == 9:
                digits += 1
                curr = start * 10 + digits
                start = curr
                diff = diff * 10 + 1
            else:
                curr = curr + diff

        return curr, start, digits, diff

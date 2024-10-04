"""
354. Russian Doll Envelopes

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of
one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll
(i.e., put one inside the other).

Note: You cannot rotate an envelope.
"""

from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], x[1]))
        max_counts = [0] * len(envelopes)

        for i in range(1, len(envelopes)):
            envelope = envelopes[i]

            # first find the position where the width is correct
            left, right = 0, i - 1
            index = -1
            while left <= right:
                mid = left + (right - left) // 2
                if envelopes[mid][0] < envelope[0]:
                    index = mid
                    left = mid + 1
                else:
                    right = mid - 1

            # now find the position for which the height is also correct
            left =


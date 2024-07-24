"""
2745. Construct the Longest New String

You are given three integers x, y, and z.

You have x strings equal to "AA", y strings equal to "BB", and z strings
equal to "AB". You want to choose some (possibly all or none) of these
strings and concatenate them in some order to form a new string. This new
string must not contain "AAA" or "BBB" as a substring.

Return the maximum possible length of the new string.

A substring is a contiguous non-empty sequence of characters within a string.
"""


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # use all the AB strings
        max_length = z * 2

        # alternatively use BB and AA for each AB string
        # example: BB AB AA
        pairs = min(x, y)
        max_length += pairs * 2 * 2

        # one remaining pair of AA can be added to the front
        # one remaining pair of BB can be appended to front
        if x > pairs or y > pairs:
            max_length += 2

        return max_length

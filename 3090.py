"""
3090. Maximum Length Substring With Two Occurrences

Given a string s, return the maximum length of a substring such that it contains
at most two occurrences of each character.
"""


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if len(s) <= 2:
            return 2

        max_length = 0
        start = 0
        curr = 0
        count_arr = [0] * 26

        while curr < len(s):
            index = ord(s[curr]) - 97
            count_arr[index] += 1
            if count_arr[index] == 3:
                max_length = max(max_length, curr - 1 - start + 1)
                while start < len(s) and count_arr[index] != 2:
                    count_arr[ord(s[start]) - 97] -= 1
                    start += 1
            curr += 1

        max_length = max(max_length, curr - 1 - start + 1)
        return max_length

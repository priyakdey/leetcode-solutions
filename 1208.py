"""
1208. Get Equal Substrings Within Budget

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of 
t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values 
of the characters).

Return the maximum length of a substring of s that can be changed to be the same 
as the corresponding substring of t with a cost less than or equal to maxCost. 
If there is no substring from s that can be changed to its corresponding 
substring from t, return 0.
"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if s is None or t is None or len(s) != len(t) or len(s) == 0:
            raise Exception("invalid arguments")

        max_length = 0
        left, right = 0, 0

        curr_cost = 0

        while right < len(s):
            curr_cost += abs(ord(s[right]) - ord(t[right]))

            if curr_cost <= maxCost:
                max_length = max(max_length, right - left + 1)
            else:
                while left <= right and curr_cost > maxCost:
                    curr_cost -= abs(ord(s[left]) - ord(t[left]))
                    left += 1

            right += 1

        return max_length

"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in 
any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_count = 0

        for i in range(k):
            if s[i] in vowels:
                max_count += 1

        curr_count = max_count

        for i in range(k, len(s)):
            if s[i] in vowels:
                curr_count += 1
            if s[i - k] in vowels:
                curr_count -= 1

            max_count = max(max_count, curr_count)

        return max_count

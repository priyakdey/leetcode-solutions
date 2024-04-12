"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower 
and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        buffer = list(s)

        left, right = 0, len(buffer) - 1

        while left < right:
            if buffer[left] in vowels and buffer[right] in vowels:
                buffer[left], buffer[right] = buffer[right], buffer[left]
                left += 1
                right -= 1
            elif buffer[left] in vowels and buffer[right] not in vowels:
                right -= 1
            elif buffer[left] not in vowels and buffer[right] in vowels:
                left += 1
            elif buffer[left] not in vowels and buffer[right] not in vowels:
                left += 1
                right -= 1

        return "".join(buffer)

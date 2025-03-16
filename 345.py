from typing import List, Set


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        buf: List[str] = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if buf[left] in vowels and buf[right] in vowels:
                buf[left], buf[right] = buf[right], buf[left]
                left += 1
                right -= 1
            elif buf[left] not in vowels:
                left += 1
            elif buf[right] not in vowels:
                right -= 1

        return "".join(buf)

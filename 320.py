"""
320. Generalized Abbreviation

A word's generalized abbreviation can be constructed by taking any number of
non-overlapping and non-adjacent substrings and replacing them with their
respective lengths.

For example, "abcde" can be abbreviated into:
- "a3e" ("bcd" turned into "3")
- "1bcd1" ("a" and "e" both turned into "1")
- "5" ("abcde" turned into "5")
- "abcde" (no substrings replaced)

However, these abbreviations are invalid:
- "23" ("ab" turned into "2" and "cde" turned into "3") is invalid as the
  substrings chosen are adjacent.
- "22de" ("ab" turned into "2" and "bc" turned into "2") is invalid as the
  substring chosen overlap.

Given a string word, return a list of all the possible generalized abbreviations of word. Return the answer in any order
"""
from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def generate(start: int, end: int, buf: List[str]) -> None:
            nonlocal abbrs

            if end == len(word):
                substring = word[start: end]
                buf.append(substring)
                abbrs.append("".join(buf))
                buf.pop()
                buf.append(str(len(substring)))
                abbrs.append("".join(buf))
                buf.pop()
                return

            generate(start, end + 1, buf)

            substring = word[start: end]
            buf.append(substring)
            generate(start + 1, end + 1, buf)
            buf.pop()
            buf.append(str(len(substring)))
            generate(start, end + 1, buf)
            buf.pop()

        abbrs: List[str] = []
        generate(0, 1, [])
        return abbrs

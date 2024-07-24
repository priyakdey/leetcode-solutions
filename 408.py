"""
408. Valid Word Abbreviation

A string can be abbreviated by replacing any number of non-adjacent, non-empty 
substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as 
(but not limited to):

- "s10n" ("s ubstitutio n")
- "sub4u4" ("sub stit u tion")
- "12" ("substitution")
- "su3i1u2on" ("su bst i t u ti on")
- "substitution" (no substrings replaced)

The following are not valid abbreviations:

- "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
- "s010n" (has leading zeros)
- "s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word is None or len(word) == 0 or abbr is None or len(abbr) == 0:
            raise Exception("invalid input")

        curr1, curr2 = 0, 0

        digit_ascii = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        while curr1 < len(word) and curr2 < len(abbr):
            if abbr[curr2] in digit_ascii:
                if abbr[curr2] == "0":
                    break
                skip = 0
                while curr2 < len(abbr) and abbr[curr2] in digit_ascii:
                    skip = skip * 10 + ord(abbr[curr2]) - 48
                    curr2 += 1

                curr1 += skip
                if curr1 >= len(word):
                    break
            elif word[curr1] != abbr[curr2]:
                break
            else:
                curr1 += 1
                curr2 += 1

        return curr1 == len(word) and curr2 == len(abbr)

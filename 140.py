"""
140. Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to
construct a sentence where each word is a valid dictionary word. Return all such
possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.
"""

from typing import List, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def generate(index: int, buf: List[List[str]]) -> None:
            nonlocal acc, words

            last_word = "".join(buf[-1])

            if index == len(s):
                if last_word in words:
                    acc.append(" ".join(["".join(x) for x in buf]))
                return

            if last_word in words:
                buf.append([s[index]])
                generate(index + 1, buf)
                buf.pop()

            buf[-1].append(s[index])
            generate(index + 1, buf)
            buf[-1].pop()

        acc: List[str] = []
        buf: List[List[str]] = [[s[0]]]
        words: Set[str] = set(wordDict)
        generate(1, buf)
        return acc

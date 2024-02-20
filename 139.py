"""
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be 
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the 
segmentation.
"""

from typing import List, Optional, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        cache: List[List[Optional[bool]]] = [
            [None for _ in range(length + 1)] for _ in range(length + 1)
        ]
        return self.word_break(s, 0, 1, set(wordDict), cache)

    def word_break(
        self,
        s: str,
        startIndex: int,
        endIndex: int,
        wordDict: Set[str],
        cache: List[List[Optional[bool]]],
    ) -> bool:
        word = s[startIndex:endIndex]

        if startIndex == len(s) - 1 or endIndex == len(s):
            return word in wordDict

        if cache[startIndex][endIndex] is not None:
            return cache[startIndex][endIndex]  # type: ignore

        can_break: bool = False

        # break at endIndex
        if word in wordDict:
            can_break = self.word_break(s, endIndex, endIndex + 1, wordDict, cache)

        # do no break at endIndex
        can_break = can_break or self.word_break(
            s, startIndex, endIndex + 1, wordDict, cache
        )

        cache[startIndex][endIndex] = can_break
        return can_break

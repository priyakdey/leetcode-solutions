"""
127. Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
  be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the
number of words in the shortest transformation sequence from beginWord to
endWord, or 0 if no such sequence exists.
"""

from typing import Dict, List, Set, Tuple


INT_MAX = (1 << 31) - 1


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def calc_distance(a: str, b: str) -> int:
            distance = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    distance += 1

            return distance

        def transform(
            curr_word: str, words_traversed: Set[str], cache: Dict[Tuple[str, ...], int]
        ) -> int:
            if curr_word == endWord:
                return 0

            if len(words_traversed) == len(wordList):
                return INT_MAX

            key = (curr_word, *words_traversed)
            if key in cache:
                return cache[key]

            count = INT_MAX

            for word in wordList:
                if word not in words_traversed and calc_distance(curr_word, word) == 1:
                    words_traversed.add(word)
                    _count = transform(word, words_traversed, cache)
                    if _count != INT_MAX:
                        count = min(count, 1 + _count)
                    words_traversed.remove(word)

            cache[key] = count
            return count

        count = transform(beginWord, set(), dict())
        return (1 + count) if count != INT_MAX else 0

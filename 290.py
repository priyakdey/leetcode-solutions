"""
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter 
in pattern and a non-empty word in s.
"""

from typing import Dict, List, Set


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        parts: List[str] = s.split(" ")
        if len(parts) != len(pattern):
            return False

        word_dict: Dict[str, str] = {}
        distinct: Set[str] = set()

        for ch, word in zip(pattern, parts):
            if ch in word_dict:
                if word != word_dict[ch]:
                    return False
            else:
                if word in distinct:
                    return False
                word_dict[ch] = word
                distinct.add(word)

        return True

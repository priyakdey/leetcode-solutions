"""
187. Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as
'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long
sequences (substrings) that occur more than once in a DNA molecule.
You may return the answer in any order.
"""

from collections import defaultdict, deque
from typing import Deque, Dict, List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        freq_map: Dict[str, int] = defaultdict(int)
        queue: Deque[str] = deque()

        for i in range(10):
            queue.append(s[i])

        freq_map["".join(queue)] += 1

        for i in range(10, len(s)):
            queue.append(s[i])
            queue.popleft()
            freq_map["".join(queue)] += 1

        words: List[str] = []
        for word, freq in freq_map.items():
            if freq > 1:
                words.append(word)

        return words

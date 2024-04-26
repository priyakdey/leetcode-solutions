"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.
"""

from typing import Dict, List


class Solution:
    # fmt: off
    primes: List[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    hash_mod: int = 1_000_000_007
    hash_seed: int = 5381
    # fmt: on

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[int, List[str]] = {}

        for s in strs:
            hash = self.calc_hash(s)
            if hash not in groups:
                groups[hash] = []
            groups[hash].append(s)

        return list(groups.values())

    def calc_hash(self, s: str) -> int:
        hash = Solution.hash_seed
        for ch in s:
            idx = ord(ch) - ord("a")
            hash = hash * Solution.primes[idx] % Solution.hash_mod
        return hash

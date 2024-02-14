"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.
"""


from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_mapping = Solution.generate_char_prime_mapping(
            [chr(i) for i in range(97, 123)]
        )

        groups: Dict[int, List[str]] = {}

        for s in strs:
            hash_code = self.calculate_hash(s, char_mapping)
            groups.setdefault(hash_code, []).append(s)

        anagram_groups: List[List[str]] = []
        for group in groups.values():
            anagram_groups.append(group)

        return anagram_groups

    def calculate_hash(self, s: str, mappings: Dict[str, int]) -> int:
        large_prime = 1_000_000_007
        h = 5381
        for c in s:
            h = (h * mappings[c]) % large_prime

        return h

    @staticmethod
    def generate_char_prime_mapping(chars: List[str]) -> Dict[str, int]:
        """Generates a map of each character to a prime number"""
        primes = Solution.generate_primes(len(chars))
        char_mapping: Dict[str, int] = {}

        for i, ch in enumerate(chars):
            char_mapping[ch] = primes[i]

        return char_mapping

    @staticmethod
    def generate_primes(n: int) -> List[int]:
        """Generates first n prime numbers"""
        primes: List[int] = [-1 for _ in range(n)]
        cursor = 0

        limit = 100
        is_prime: List[bool] = [True for _ in range(limit + 1)]

        is_prime[0] = False
        is_prime[1] = False

        while cursor < n:
            # sieve new numbers
            start = 2
            for i in range(start, limit + 1):
                if is_prime[i]:
                    j = 2
                    while i * j <= limit:
                        is_prime[i * j] = False
                        j += 1

            # accumulate all primes
            i = start
            while i <= limit and cursor < n:
                if is_prime[i]:
                    primes[cursor] = i
                    cursor += 1
                i += 1

            # resize limit if necessary
            if cursor < n:
                curr_end = limit
                limit = limit << 1
                is_prime = is_prime + [True for _ in range(curr_end + 1, limit + 1)]
                start = curr_end

        return primes

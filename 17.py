"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given 
below. Note that 1 does not map to any letters.
"""

from typing import Dict, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def generate_combinations(index: int, buffer: List[str]) -> None:
            nonlocal digits
            nonlocal mappings
            nonlocal combinations

            if index == len(digits):
                combinations.append("".join(buffer))
                return

            digit = digits[index]
            for ch in mappings[digit]:
                buffer.append(ch)
                generate_combinations(index + 1, buffer)
                buffer.pop()

        if len(digits) == 0:
            return []

        mappings: Dict[str, List[str]] = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        combinations: List[str] = []
        generate_combinations(0, [])
        return combinations

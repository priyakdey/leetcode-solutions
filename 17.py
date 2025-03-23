from typing import Dict, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def generate(index: int, buf: List[str], i: int) -> None:
            nonlocal digits, mappings, combinations

            if index == len(digits):
                combinations.append("".join(buf))
                return

            for ch in mappings[digits[index]]:
                buf[i] = ch
                generate(index + 1, buf, i + 1)

        mappings: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) == 0:
            return []

        combinations: List[str] = []
        buf: List[str] = [""] * len(digits)
        generate(0, buf, 0)
        return combinations

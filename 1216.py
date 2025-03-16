from typing import Dict, Tuple


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def is_valid(left: int, right: int, k: int) -> bool:
            nonlocal s, cache

            if left >= right:
                return True

            key = (left, right, k)
            if key in cache:
                return cache[key]

            if s[left] == s[right]:
                return is_valid(left + 1, right - 1, k)

            if k == 0:
                return False

            valid = is_valid(left + 1, right, k - 1) or is_valid(left, right - 1, k - 1)
            cache[key] = valid
            return valid

        cache: Dict[Tuple[int, int, int], bool] = {}
        return is_valid(0, len(s) - 1, k)

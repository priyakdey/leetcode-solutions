class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid(left: int, right: int, can_delete: bool) -> bool:
            nonlocal s

            if left >= right:
                return True

            if s[left] == s[right]:
                return is_valid(left + 1, right - 1, can_delete)

            if not can_delete:
                return False

            return is_valid(left + 1, right, not can_delete) or is_valid(
                left, right - 1, not can_delete
            )

        return is_valid(0, len(s) - 1, True)

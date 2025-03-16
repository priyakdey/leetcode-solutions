class Solution:
    def makePalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        operations = 2

        while left < right:
            if s[left] != s[right]:
                operations -= 1
            left += 1
            right -= 1

        return operations >= 0

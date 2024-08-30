class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        for i in range(len(s)):
            for j in range
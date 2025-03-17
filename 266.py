from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq_table = Counter(s)
        odd_count = 0
        for freq in freq_table.values():
            if (freq & 1) == 1:
                odd_count += 1

        return odd_count < 2

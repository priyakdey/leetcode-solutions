from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq_table = Counter(nums)
        for freq in freq_table.values():
            if (freq & 1) == 1:
                return False

        return True

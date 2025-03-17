from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_table = Counter(arr)
        seen: Set[int] = set()
        for freq in freq_table.values():
            if freq in seen:
                return False
            seen.add(freq)

        return True

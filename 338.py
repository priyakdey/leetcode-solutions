from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_count_arr: List[int] = [0] * (n + 1)

        shift: int = 0
        for i in range(1, n + 1):
            if i == (1 << shift):
                bit_count_arr[i] = 1
                shift += 1
            else:
                bit_count_arr[i] = 1 + bit_count_arr[i - (1 << (shift - 1))]

        return bit_count_arr

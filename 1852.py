from typing import Dict, List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        count: List[int] = [0] * (len(nums) - k + 1)
        freq_map: Dict[int, int] = {}
        for i in range(k):
            num = nums[i]
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1

        count[0] = len(freq_map)

        for i in range(k, len(nums)):
            num = nums[i]
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1

            freq_map[nums[i - k]] -= 1
            if freq_map[nums[i - k]] == 0:
                del freq_map[nums[i - k]]

            count[i - k + 1] = len(freq_map)

        return count

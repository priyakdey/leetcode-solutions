from tying import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_height = 0
        max_height = 0

        for delta in gain:
            curr_height += delta
            max_height = max(max_height, curr_height)

        return max_height

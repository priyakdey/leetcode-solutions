from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = -1
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] > target:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return letters[index] if index != -1 else letters[0]

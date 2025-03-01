# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            pick = left + (right - left) // 2
            result = guess(pick)
            if result == 0:
                return pick
            elif result == 1:
                left = pick + 1
            else:
                right = pick - 1

        raise Exception("invalid input")

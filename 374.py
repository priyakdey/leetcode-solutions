"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is 
higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:
- -1: Your guess is higher than the number I picked (i.e. num > pick).
- 1: Your guess is lower than the number I picked (i.e. num < pick).
- 0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.
"""


def guess(num: int) -> int:  # type: ignore
    """The guess API is already defined for you.
    @param num, your guess
    @return -1 if num is higher than the picked number
            1 if num is lower than the picked number
            otherwise return 0
    """
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        guessed_number = -1
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            is_right = guess(mid)
            if is_right == 0:
                guessed_number = mid
                break
            elif is_right == -1:
                right = mid - 1
            else:
                left = mid + 1

        return guessed_number

"""
367. Valid Perfect Square

Given a positive integer num, return true if num is a perfect square or 
false otherwise.

A perfect square is an integer that is the square of an integer. 
In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num

        while left <= right:
            mid = left + (right - left) // 2
            value = mid * mid
            if value == num:
                return True
            elif value > num:
                right = mid - 1
            else:
                left = mid + 1

        return False

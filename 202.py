"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the 
squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops 
endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def _next(x: int):
            summ = 0
            while x != 0:
                summ += (x % 10) ** 2
                x //= 10

            print(summ)
            return summ

        slow_pointer = n
        fast_pointer = _next(n)

        if fast_pointer == 1:
            return True

        while fast_pointer != slow_pointer and fast_pointer != 1:
            slow_pointer = _next(slow_pointer)
            fast_pointer = _next(_next(fast_pointer))

        return fast_pointer == 1

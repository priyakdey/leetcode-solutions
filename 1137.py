class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1

        if n == 0:
            return a
        if n == 1:
            return b
        if n == 2:
            return c

        for _ in range(2, n):
            x = a + b + c
            a = b
            b = c
            c = x

        return c

"""
3179. Find the N-th Value After K Seconds

You are given two integers n and k.

Initially, you start with an array a of n integers where a[i] = 1 for all
0 <= i <= n - 1. After each second, you simultaneously update each element to
be the sum of all its preceding elements plus the element itself.
For example, after one second, a[0] remains the same,
a[1] becomes a[0] + a[1], a[2] becomes a[0] + a[1] + a[2], and so on.

Return the value of a[n - 1] after k seconds.

Since the answer may be very large, return it modulo 10^9 + 7.
"""


class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        curr_state, next_state = [1] * n, [1] * n

        for i in range(k):
            for j in range(1, n):
                next_state[j] = next_state[j - 1] + curr_state[j]
                next_state[j] = next_state[j] % MOD
                curr_state = next_state

        return next_state[-1]

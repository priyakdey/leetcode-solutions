class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        x = 0
        while left <= right:
            mid = left + (right - left) // 2
            if mid * (mid + 1) // 2 <= n:
                x = mid
                left = mid + 1
            else:
                right = mid - 1
        return x


class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = -1
        
        left, right = 0, x // 2 + 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                sqrt = mid
                left = mid + 1
            else:
                right = mid - 1

        return sqrt


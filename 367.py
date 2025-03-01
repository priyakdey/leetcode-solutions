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



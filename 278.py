# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        first_bad_version = -1

        while left <= right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                first_bad_version = mid
                right = mid - 1
            else:
                left = mid + 1

        if first_bad_version == -1:
            # exception because the the problem statement always expects a bad version
            raise Exception("no bad version found")

        return first_bad_version


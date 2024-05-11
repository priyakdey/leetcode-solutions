"""
278. First Bad Version

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions 
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version 
is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API.
"""


def isBadVersion(version: int) -> bool:  # type: ignore
    """The isBadVersion API is already defined for you."""
    pass


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

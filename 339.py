"""
339. Nested List Weight Sum

You are given a nested list of integers nestedList. Each element is either an 
integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. 
For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set 
to its depth.

Return the sum of each integer in nestedList multiplied by its depth.
"""

from typing import List


class NestedInteger:
    """
    This is the interface that allows for creating nested lists.
    You should not implement it, or speculate about its implementation
    """

    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.depthSum_internal(nestedList, 1)

    def depthSum_internal(self, nestedList: List[NestedInteger], depth: int) -> int:
        sum = 0

        for nestedInteger in nestedList:
            if nestedInteger.isInteger():
                sum += depth * nestedInteger.getInteger()  # type: ignore
            else:
                sum += self.depthSum_internal(nestedInteger.getList(), depth + 1)  # type: ignore

        return sum

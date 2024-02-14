"""
1265. Print Immutable Linked List in Reverse

You are given an immutable linked list, print out all values of each node in 
reverse with the help of the following interface:

ImmutableListNode: An interface of immutable linked list, you are given the 
head of the list.
You need to use the following functions to access the linked list 
(you can't access the ImmutableListNode directly):

ImmutableListNode.printValue(): Print value of the current node.
ImmutableListNode.getNext(): Return the next node.

The input is only given to initialize the linked list internally. 
You must solve this problem without modifying the linked list. 
In other words, you must operate the linked list using only the mentioned APIs.
"""


class ImmutableListNode:
    """
    This is the ImmutableListNode's API interface.
    You should not implement it, or speculate about its implementation.
    """

    def printValue(self) -> None:  # print the value of this node.
        pass

    def getNext(self) -> "ImmutableListNode":  # return the next node.
        pass


class Solution:
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        if head is None:
            return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()

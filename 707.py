"""
707. Design Linked List

Design your implementation of the linked list. You can choose to use a singly 
or doubly linked list.
A node in a singly linked list should have two attributes: val and next. 
val is the value of the current node, and next is a pointer/reference to the 
next node.
If you want to use the doubly linked list, you will need one more attribute 
prev to indicate the previous node in the linked list. 
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the index-th node in the linked list. 
  If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of 
  the linked list. After the insertion, the new node will be the first node of 
  the linked list.
- void addAtTail(int val) Append a node of value val as the last element of the 
  linked list.
- void addAtIndex(int index, int val) Add a node of value val before the index-th 
  node in the linked list. If index equals the length of the linked list, the 
  node will be appended to the end of the linked list. 
  If index is greater than the length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the indexth node in the linked list, 
  if the index is valid.
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head: Node = Node(-1)  # Dummy node (sentinel)
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next  # type: ignore

        return curr.val  # type: ignore

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node  # type: ignore
        self.length += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(val)  # type: ignore
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next  # type: ignore

        new_node = Node(val)
        new_node.next = prev.next  # type: ignore
        prev.next = new_node  # type: ignore
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next  # type: ignore

        prev.next = prev.next.next  # type: ignore
        self.length -= 1

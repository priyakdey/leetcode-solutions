"""
716. Max Stack

Design a max stack data structure that supports the stack operations and 
supports finding the stack's maximum element.

Implement the MaxStack class:

- MaxStack() Initializes the stack object.
- void push(int x) Pushes element x onto the stack.
- int pop() Removes the element on top of the stack and returns it.
- int top() Gets the element on the top of the stack without removing it.
- int peekMax() Retrieves the maximum element in the stack without removing it.
- int popMax() Retrieves the maximum element in the stack and removes it. 
  If there is more than one maximum element, only remove the top-most one.

You must come up with a solution that supports O(1) for each top call 
and O(logn) for each other call.
"""

from typing import List, Optional, Tuple, cast


class Node:

    def __init__(self, val: int):
        self.val = val
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

    def __gt__(self, that) -> bool:
        return self.val > that.val


class MaxHeap:

    def __init__(self):
        self.heap: List[Node] = []

    def push(self, node: Node) -> None:
        self.heap.append(node)

        if len(self.heap) == 1:
            return

        curr_index = len(self.heap) - 1

        while curr_index > 0:
            parent_index = self.get_parent_index(curr_index)
            child_node = self.heap[curr_index]
            parent_node = self.heap[parent_index]
            if child_node > parent_node:
                self.swap(curr_index, parent_index)
            else:
                break

            curr_index = parent_index

    def pop(self) -> Node:
        if len(self.heap) == 1:
            return self.heap.pop(0)

        root = self.heap[0]
        self.swap(0, len(self.heap) - 1)

        curr_index = 0
        while curr_index < len(self.heap):
            left_index, right_index = self.get_child_index(curr_index)

            if left_index >= len(self.heap):
                break

            swap_index = left_index

            if (
                right_index < len(self.heap)
                and self.heap[right_index] > self.heap[left_index]
            ):
                swap_index = right_index

            if self.heap[swap_index] > self.heap[curr_index]:
                self.swap(swap_index, curr_index)
            else:
                break

            curr_index = swap_index

        return root

    def peek(self) -> int:
        return self.heap[0].val

    def swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def get_child_index(self, index: int) -> Tuple[int, int]:
        return 2 * index + 1, 2 * index + 2


class Stack:

    def __init__(self):
        self.bottom: Optional[Node] = None
        self.top: Optional[Node] = None
        self.size = 0

    def push(self, val: int) -> Node:
        node = Node(val)
        if self.size == 0:
            self.bottom = self.top = node
            self.top = self.top = node
        else:
            cast(Node, self.top).next = node
            node.prev = self.top
            self.top = node
        self.size += 1

        return node

    def pop(self) -> int:
        if self.size == 0:
            raise Exception("invalid argument")

        top = self.top
        prev = cast(Node, self.top).prev
        cast(Node, prev).next = None
        self.top = prev
        self.size -= 1
        return cast(Node, top).val

    def remove_node(self, node: Node) -> None:
        if node is self.bottom:
            self.bottom = self.bottom.next
            self.bottom.prev = None
            self.size -= 1
        elif node is self.top:
            self.pop()
        else:
            prev = self.node.prev
            next = self.node.next
            prev.next = next
            next.prev = prev
            self.size -= 1

    def peek(self) -> int:
        return cast(Node, self.top).val


class MaxStack:

    def __init__(self):
        self.stack: Stack = Stack()
        self.heap: MaxHeap = MaxHeap()

    def push(self, x: int) -> None:
        node = self.stack.push(x)
        self.heap.push(node)

    def pop(self) -> int:
        node = self.stack.pop()
        return node.val

    def top(self) -> int:
        return self.stack.peek()

    def peekMax(self) -> int:
        return self.heap.peek()

    def popMax(self) -> int:
        node = self.heap.pop()
        self.stack.remove_node(node)
        return node.val

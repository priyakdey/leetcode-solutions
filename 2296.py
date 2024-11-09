"""
2296. Design a Text Editor

Design a text editor with a cursor that can do the following:

- Add text to where the cursor is.
- Delete text from where the cursor is (simulating the backspace key).
- Move the cursor either left or right.

When deleting text, only characters to the left of the cursor will be deleted.
The cursor will also remain within the actual text and cannot be moved beyond
it. More formally, we have that 0 <= cursor.position <= currentText.length
always holds.

Implement the TextEditor class:

- TextEditor() Initializes the object with empty text.
- void addText(string text) Appends text to where the cursor is.
  The cursor ends to the right of text.
- int deleteText(int k) Deletes k characters to the left of the cursor.
  Returns the number of characters actually deleted.
- string cursorLeft(int k) Moves the cursor to the left k times. Returns the
  last min(10, len) characters to the left of the cursor, where len is the
  number of characters to the left of the cursor.
- string cursorRight(int k) Moves the cursor to the right k times. Returns the
  last min(10, len) characters to the left of the cursor, where len is the
  number of characters to the left of the cursor.
"""

from typing import List, Optional


class Node:

    def __init__(self, ch: str):
        self.ch = ch
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class TextEditor:

    def __init__(self):
        self.head: Node = Node("")
        self.tail: Node = Node("")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.cursor: Node = self.head

    def addText(self, text: str) -> None:
        next_node = self.cursor.next

        for ch in text:
            node = Node(ch)
            self.cursor.next = node
            node.prev = self.cursor
            self.cursor = self.cursor.next
            self.size += 1

        self.cursor.next = next_node
        next_node.prev = self.cursor
        print(self)

    def deleteText(self, k: int) -> int:
        next_node = self.cursor.next
        deleted: int = 0
        while self.cursor != self.head and k > 0:
            self.cursor = self.cursor.prev
            self.size -= 1
            deleted += 1
            k -= 1

        self.cursor.next = next_node
        next_node.prev = self.cursor
        print(self)
        return deleted

    def cursorLeft(self, k: int) -> str:
        while self.cursor != self.head and k > 0:
            self.cursor = self.cursor.prev
            k -= 1

        print(self)
        return self.__text()

    def cursorRight(self, k: int) -> str:
        while self.cursor != self.tail and k > 0:
            print(self)
            self.cursor = self.cursor.next
            k -= 1

        print(self)
        return self.__text()

    def __text(self) -> str:
        curr = self.cursor
        i = 0
        buf: List[str] = []
        while curr != self.head and i < 11:
            buf.append(curr.ch)
            curr = curr.prev

        return "".join(buf[::-1])

    def __str__(self):
        curr = self.head
        buf = []
        while curr != self.tail:
            buf.append(curr.ch)
            curr = curr.next

        return f"self.cursor is at : {self.cursor.ch} and text = {"".join(buf)}"


s = TextEditor()
s.addText("leetcode")
print("======================")
print(s.deleteText(4))
print("======================")
s.addText("practice")
print("======================")
print(s.cursorRight(3))

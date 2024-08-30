"""
212. Word Search II

Given an m x n board of characters and a list of strings words, return all
words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.
"""

from typing import List, Optional, Tuple


class Node:

    def __init__(self, parent: Optional["Node"] = None):
        self.children: List[Optional[Node]] = [None] * 26
        self.end = False
        self.parent = parent


class Trie:

    def __init__(self):
        self.root = Node()
        self.cursor = self.root

    def add_all(self, words: List[str]) -> None:
        for word in words:
            self.push(word)

    def push(self, word: str) -> None:
        curr = self.root
        for ch in word:
            index = ord(ch) - ord("a")
            if curr.children[index] is None:
                curr.children[index] = Node(curr)
            curr = curr.children[index]

        curr.end = True

    def can_move_fwd(self, ch: str) -> bool:
        index = ord(ch) - ord("a")
        return self.cursor.children[index] is not None

    def traverse_fwd(self, ch: str) -> None:
        index = ord(ch) - ord("a")
        self.cursor = self.cursor.children[index]

    def traverse_back(self) -> None:
        self.cursor = self.cursor.parent

    def is_word(self) -> bool:
        return self.cursor.end

    def mark_word_as_used(self) -> None:
        self.cursor.end = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def find(row: int, col: int, buf: List[str]) -> None:
            nonlocal rows, cols, trie, acc, directions

            if trie.is_word():
                acc.append("".join(buf))
                trie.mark_word_as_used()

            if (
                    row < 0
                    or row >= rows
                    or col < 0
                    or col >= cols
                    or board[row][col] == "-"
            ):
                return

            ch = board[row][col]

            if not trie.can_move_fwd(ch):
                return

            buf.append(ch)
            board[row][col] = "-"
            trie.traverse_fwd(ch)
            for dy, dx in directions:
                find(row + dy, col + dx, buf)

            buf.pop()
            trie.traverse_back()
            board[row][col] = ch

        rows, cols = len(board), len(board[0])
        trie = Trie()
        trie.add_all(words)
        acc: List[str] = []
        directions: List[Tuple[int, int]] = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for row in range(rows):
            for col in range(cols):
                find(row, col, [])

        return acc

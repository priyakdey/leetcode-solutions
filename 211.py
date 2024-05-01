"""
211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string 
matches any previously added string.

Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure 
  that matches word or false otherwise. word may contain dots '.' where dots 
  can be matched with any letter.
"""

from typing import List, Optional, cast


class Node:

    def __init__(self):
        self.children: List[Optional[Node]] = [None for _ in range(26)]
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            return

        curr = self.root

        for ch in word:
            idx = ord(ch) - 97
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = cast(Node, curr.children[idx])

        curr.isWord = True

    def search(self, word: str) -> bool:
        return self.search_word(self.root, word, 0)

    def search_word(self, node: Node, word: str, index: int) -> bool:
        if index == len(word):
            return node.isWord

        ch = word[index]
        idx = ord(ch) - 97

        is_match = False

        match ch:
            case ".":
                for child_node in node.children:
                    if child_node is not None and self.search_word(
                        child_node, word, index + 1
                    ):
                        is_match = True
                        break
            case _:
                child_node = node.children[idx]
                is_match = child_node is not None and self.search_word(
                    child_node, word, index + 1
                )

        return is_match

"""
208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to 
efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, 
such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie 
  (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously 
  inserted string word that has the prefix prefix, and false otherwise.
"""

from typing import List, Optional


class Trie:

    def __init__(self):
        self.root: Node = Node("")

    def insert(self, word: str) -> None:
        if word == "":
            return

        curr: Node = self.root
        for ch in word:
            index = ord(ch) - 97
            if curr.children[index] is None:
                curr.children[index] = Node(ch)
            curr = curr.children[index]  # type: ignore

        curr.end = True

    def search(self, word: str) -> bool:
        if word == "":
            return False

        curr: Node = self.root
        for ch in word:
            index = ord(ch) - 97
            if curr.children[index] is None:
                return False
            curr = curr.children[index]  # type: ignore

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        if prefix is None:
            return True

        curr: Node = self.root
        for ch in prefix:
            index = ord(ch) - 97
            if curr.children[index] is None:
                return False
            curr = curr.children[index]  # type: ignore

        return True


class Node:

    def __init__(self, ch: str):
        self.ch = ch
        self.children: List[Optional[Node]] = [None for _ in range(26)]
        self.end = False

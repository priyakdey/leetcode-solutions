"""
648. Replace Words

In English, we have a concept called root, which can be followed by some other 
word to form another longer word - let's call this word derivative. 
For example, when the root "help" is followed by the word "ful", we can 
form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words 
separated by spaces, replace all the derivatives in the sentence with the root 
forming it. If a derivative can be replaced by more than one root, replace it 
with the root that has the shortest length.

Return the sentence after the replacement.
"""

from typing import List, Optional, cast


class Node:
    def __init__(self):
        self.children: List[Optional[Node]] = [None] * 26
        self.eow = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word: str) -> None:
        if len(word) == 0:
            return

        curr = self.root

        for ch in word:
            index = ord(ch) - 97
            if curr.children[index] is None:
                curr.children[index] = Node()

            curr = cast(Node, curr.children[index])

        curr.eow = True

    def prefix(self, word: str) -> str:
        cursor = 0
        curr = self.root

        while cursor < len(word):
            ch = word[cursor]
            index = ord(ch) - 97
            if curr.eow is True or curr.children[index] is None:
                break
            curr = cast(Node, curr.children[index])
            cursor += 1

        return word[:cursor] if curr.eow else ""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.add(word)

        words = sentence.split(" ")

        for i, word in enumerate(words):
            prefix = trie.prefix(word)
            if prefix != "":
                words[i] = prefix

        return " ".join(words)

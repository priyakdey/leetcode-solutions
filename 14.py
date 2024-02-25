"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of 
strings.

If there is no common prefix, return an empty string "".
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        trie = Trie()
        for word in strs:
            trie.add_word(word)

        return trie.longest_prefix()


class Node:
    def __init__(self) -> None:
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word) -> None:
        if len(word) == 0:
            self.root.is_word = True
            return

        curr = self.root
        for ch in word:
            if len(curr.children) == 0 or ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.is_word = True

    def longest_prefix(self) -> str:
        curr = self.root
        longest_prefix: List[str] = []
        while curr is not None and len(curr.children) == 1 and curr.is_word is False:
            for ch, node in curr.children.items():
                # TODO: only 1 should be present. There must be a better way to unpack dict_keys
                longest_prefix.append(ch)
                curr = node
        return "".join(longest_prefix)

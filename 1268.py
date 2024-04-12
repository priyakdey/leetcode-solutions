"""
1268. Search Suggestions System

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after 
each character of searchWord is typed. Suggested products should have common 
prefix with searchWord. If there are more than three products with a common 
prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of 
searchWord is typed.
"""

from typing import List, Optional, cast


class Node:

    def __init__(self):
        self.children: List[Optional[Node]] = [None for _ in range(0, 26)]
        self.isWord: bool = False


class Trie:

    def __init__(self):
        self.root: Node = Node()

    def add(self, word: str) -> None:
        if len(word) == 0:
            return

        curr = self.root
        for ch in word:
            index = ord(ch) - 97
            if curr.children[index] is None:
                curr.children[index] = Node()
            curr = cast(Node, curr.children[index])

        curr.isWord = True

    def suggest(self, prefix: str) -> List[str]:
        if len(prefix) == 0:
            return []

        curr = self.root
        for ch in prefix:
            index = ord(ch) - 97
            if curr.children[index] is None:
                return []
            curr = cast(Node, curr.children[index])

        suggestions: List[str] = []
        k = 3

        self._dfs(curr, k, [prefix], suggestions)
        return suggestions

    def _dfs(
        self, node: Node, k: int, buffer: List[str], suggestions: List[str]
    ) -> None:
        if len(suggestions) == k:
            return

        if node.isWord:
            suggestions.append("".join(buffer))

        for index, children in enumerate(node.children):
            if children is not None:
                ch = chr(index + 97)
                buffer.append(ch)
                self._dfs(children, k, buffer, suggestions)
                buffer.pop()


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.add(product)

        suggestions: List[List[str]] = []

        for i in range(1, len(searchWord) + 1):
            suggestions.append(trie.suggest(searchWord[:i]))

        return suggestions

"""
249. Group Shifted Strings

Perform the following shift operations on a string:

Right shift: Replace every letter with the successive letter of the English
alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted
to "bcd" or "xyz" can be right-shifted to "yza".

Left shift: Replace every letter with the preceding letter of the English
alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted
to "abc" or "yza" can be left-shifted to "xyz".

We can keep shifting the string in both directions to form an endless shifting sequence.

For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ...
<-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...

You are given an array of strings strings, group together all strings[i] that
belong to the same shifting sequence. You may return the answer in any order.
"""

from typing import Dict, List, Tuple

type Key = Tuple[int, Tuple[int, ...]]


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def calc_key(s: str) -> Key:
            diff: List[int] = [0] * (len(s) - 1)
            for i in range(1, len(s)):
                diff[i - 1] = (ord(s[i]) - ord(s[i - 1])) % 26

            return len(s), tuple(diff)

        group_dict: Dict[Key, List[str]] = {}
        for s in strings:
            key = calc_key(s)
            if key not in group_dict:
                group_dict[key] = []
            group_dict[key].append(s)

        groups: List[List[str]] = [list()] * len(group_dict)
        curr = 0
        for _, group in group_dict.items():
            groups[curr] = group
            curr += 1

        return groups

"""
678. Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')' and '*', 
return true if s is valid.

The following rules define a valid string:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left 
  parenthesis '(' or an empty string "".
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        left_balance = 0
        for char in s:
            if char in "(*":
                left_balance += 1
            else:
                left_balance -= 1
            if left_balance < 0:
                return False

        if left_balance == 0:
            return True

        right_balance = 0
        for char in reversed(s):
            if char in ")*":
                right_balance += 1
            else:
                right_balance -= 1
            if right_balance < 0:
                return False

        return True

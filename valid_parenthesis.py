# https://leetcode.com/problems/valid-parentheses/
"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and
      ']', determine if the input string is valid.

    An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

    Example 1:

    Input: s = "()"
    Output: true

    Example 2:

    Input: s = "()[]{}"
    Output: true

    Example 3:

    Input: s = "(]"
    Output: false

"""


class Solution:
    characters: dict[str, str] = {'(': ')', '{': '}', '[': ']'}

    def isValid(self, s: str) -> bool:
        opened: list[str] = []
        for i in range(len(s)):
            if s[i] in self.characters.keys():
                opened.append(s[i])
            elif s[i] in self.characters.values():
                if opened and self.characters[opened[-1]] == s[i]:
                    del opened[-1]
                else:
                    return False

        if opened:
            return False
        return True


if __name__ == '__main__':
    a = Solution()
    assert a.isValid("()[]{}") is True
    assert a.isValid("([]{})") is True
    assert a.isValid("({)[]}") is False
    assert a.isValid("(){[]}") is True
    assert a.isValid("((){[]}") is False

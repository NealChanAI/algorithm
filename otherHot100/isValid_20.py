# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-02 14:40
#    @Description   : #20
#
# ===============================================================


"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""


class Solution:
    def isValid(self, s):
        """
        栈
        """
        if not s:
            return

        pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        left = []
        for c in s:
            if c in ('(', '[', '{'):
                left.append(c)
            else:
                if left and left[-1] == pair[c]:
                    left.pop()
                else:
                    return False
        return True if not left else False


if __name__ == '__main__':
    s = "()"
    # s = "()[]{}"
    # s = "(]"
    s = "([])"

    print(Solution().is_valid(s))

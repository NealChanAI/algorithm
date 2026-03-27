# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 12:48
#    @Description   : 
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
        """栈实现"""
        left = []
        _m = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for i in range(len(s)):
            if s[i] in ['{', '(', '[']:
                left.append(s[i])
            else:
                if left and left[-1] == _m[s[i]]:
                    left.pop()
                else:
                    return False

        return False if left else True

# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/14 19:19
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
        if not s:
            return

        d = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        left = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                left.append(s[i])
            else:
                if left and left[-1] == d[s[i]]:
                    left.pop()
                else:
                    return False

        return True if not left else False

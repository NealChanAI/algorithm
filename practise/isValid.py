# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 08:54
#    @Description   : 
#
# ===============================================================


class Solution:
    def isValid(self, s):
        """使用栈实现"""
        if not s:
            return

        left = []
        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in ('(', '{', '['):
                left.append(c)
            else:
                if left and match[c] == left[-1]:
                    left.pop()
                else:
                    return False
        return True if not left else False

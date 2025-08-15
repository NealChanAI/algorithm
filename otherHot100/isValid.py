# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


class Solution:
    def isValid(self, s):
        """

        :param s:
        :return:
        """
        if not s:
            return

        pair = {"}": "{", "]": "[", ")": "("}
        left = []
        for c in s:
            if c in ["(", "{", "["]:
                left.append(c)
            else:
                if left and pair[c] == left[-1]:
                    left.pop()
                else:
                    return False

        return True if not left else False

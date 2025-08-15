# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/18 00:40
#    @Description   : 22. 括号生成
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def generateParenthesis(self, n):
        """
        back track algo.
        rule: 括号组成的字符串p中，p[:i]中左括号的数量肯定是大于等于右括号的
        :return:
        """
        if not n or n < 0:
            return

        self.back_track(n, n)
        return self.res

    def back_track(self, left, right):
        """

        :param left: 还剩下多少个left可以使用
        :param right: 还剩下多少个left可以使用
        :return:
        """
        if left < 0 or right < 0:
            return

        if left > right:
            return

        if left == 0 and right == 0:
            self.res.append("".join(self.path.copy()))

        self.path.append("(")
        self.back_track(left - 1, right)
        self.path.pop()

        self.path.append(")")
        self.back_track(left, right - 1)
        self.path.pop()


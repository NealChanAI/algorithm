# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-15 17:37
#    @Description   : 
#
# ===============================================================


"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
"""


class Solution:
    def __init__(self):
        self.memo = []

    def minDistance(self, s1, s2):
        """
        dp:
            base case: 抵达边界 或 两个字符相等
        memo
        """

        if not s1 and not s2:
            return 0

        p1, p2 = len(s1) - 1, len(s2) - 1
        res = float('inf')
        m, n = len(s1), len(s2)
        self.memo = [[-1] * n for _ in range(m)]

        return self.dp(s1, s2, p1, p2)

    def dp(self, s1, s2, i, j):
        """dp数组"""
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, s2, i-1, j-1)
            return self.memo[i][j]

        self.memo[i][j] = min(
                self.dp(s1, s2, i - 1, j),
                self.dp(s1, s2, i - 1, j - 1),
                self.dp(s1, s2, i, j - 1)
            ) + 1

        return self.memo[i][j]


# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 12:49
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
        dp实现
            从右往左
        """
        self.memo = [[-1] * len(s2) for _ in range(len(s1))]

        return self.dp(s1, s2, len(s1) - 1, len(s2) - 1)

    def dp(self, s1, s2, i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        if s1[i] == s2[j]:
            return self.dp(s1, s2, i - 1, j - 1)

        self.memo[i][j] = 1 + min(
            self.dp(s1, s2, i - 1, j),
            self.dp(s1, s2, i, j - 1),
            self.dp(s1, s2, i - 1, j - 1)
        )

        return self.memo[i][j]


if __name__ == '__main__':
    s1 = "dinitrophenylhydrazine"
    s2 = "benzalphenylhydrazone"
    res = Solution().minDistance(s1, s2)
    print(res)
# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-01-04 14:37
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
    def minDistance(self, s1, s2):
        """
        1. 非空判断
        2. memo备忘录
        """
        if not s1 and not s2:
            return 0

        m, n = len(s1), len(s2)
        memo = [[-1] * n for _ in range(m)]

        def dp(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if memo[i][j] != -1:
                return memo[i][j]

            if s1[i] == s2[j]:
                memo[i][j] = dp(i-1, j-1)
            else:
                memo[i][j] = 1 + min(
                    dp(i-1, j),
                    dp(i, j-1),
                    dp(i-1, j-1)
                )

            return memo[i][j]

        return dp(m-1, n-1)


if __name__ == '__main__':
    s1 = "dinitrophenylhydrazine"
    s2 = "benzalphenylhydrazone"
    res = Solution().minDistance(s1, s2)
    print(res)
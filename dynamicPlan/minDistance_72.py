# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/9 21:43
#    @Description   : #72
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
        if not s1 or not s2:
            return

        m, n = len(s1), len(s2)
        return self.dp(s1, s2, m-1, n-1)

    def dp(self, s1, s2, i, j):
        if i <= -1:
            return j + 1
        if j <= -1:
            return i + 1
        if s1[i] == s2[j]:
            return self.dp(s1, s2, i-1, j-1)

        return 1 + min(
            self.dp(s1, s2, i-1, j),
            self.dp(s1, s2, i-1, j-1),
            self.dp(s1, s2, i, j-1)
        )

if __name__ == '__main__':
    s1 = "dinitrophenylhydrazine"
    s2 = "benzalphenylhydrazone"
    Solution().minDistance(s1, s2)

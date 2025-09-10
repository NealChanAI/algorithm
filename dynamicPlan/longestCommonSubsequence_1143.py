# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/9 22:09
#    @Description   : #1143
#
# ===============================================================


"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

示例 1：
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
"""


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        """

        """
        if not text1 and not text2:
            return

        memo = [[-1] * len(text2) for _ in range(len(text1))]

        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            if text1[i] == text2[j]:
                memo[i][j] = dp(i+1, j+1) + 1
            else:
                memo[i][j] = max(dp(i+1, j), dp(i, j+1), dp(i+1, j+1))

            return memo[i][j]

        return dp(0, 0)


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    res = Solution().longestCommonSubsequence(text1, text2)
    print(res)

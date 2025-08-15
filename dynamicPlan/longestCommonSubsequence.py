# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/2 16:04
#    @Description   : 1143. 最长公共子序列
#
# ===============================================================


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        """
        :param text1:
        :param text2:
        :return:
        """
        memo = [[-1] * len(text2) for _ in len(text1)]

        def dp(i, j):
            # base case
            if i < 0 or j < 0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if text1[i] == text2[j]:
                return dp(i-1, j-1) + 1

            memo[i][j] = max(dp(i-1, j),
                       # dp(i-1, j-1),
                       dp(i, j-1)
                       )
            return memo[i][j]
        return dp(len(text1)-1, len(text2)-1)

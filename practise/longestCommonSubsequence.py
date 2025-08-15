# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 18:00
#    @Description   : 
#
# ===============================================================


class Solution:
    def longestCommonSubsequence(self,text1, text2):
        """
        动态规划：
            1. 指针指向-1时，返回0
        :param text1:
        :param text2:
        :return:
        """

        memo = [[-1] * len(text2) for _ in range(len(text1))]

        def dp(i, j):
            # base case
            if i < 0 or j < 0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if text1[i] == text2[j]:
                return dp(i - 1, j - 1) + 1

            memo[i][j] = max(dp(i - 1, j - 1),  # text1[i]和text2[j]均不在最长公共序列中)
                dp(i - 1, j),  # text1[i]不在最长公共序列中
                dp(i, j - 1))  # text2[j]不在最长公共序列中
            return memo[i][j]

        return dp(len(text1) - 1, len(text2) - 1)


if __name__ == '__main__':
    text1 = 'abcde'
    text2 = 'ace'
    text1 = 'abc'
    text2 = 'abc'
    print(Solution().longestCommonSubsequence(text1, text2))
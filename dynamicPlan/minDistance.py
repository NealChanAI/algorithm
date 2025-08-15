# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/2 15:07
#    @Description   : 72. 编辑距离
#
# ===============================================================


class Solution:
    def minDistance(self, word1, word2):
        """
        dp
        :param word1:
        :param word2:
        :return:
        """
        memo = [[-1] * len(word2) for _ in range(len(word1))]

        def dp(i, j):
            # base case
            if j < 0:
                return i + 1
            if i < 0:
                return j + 1

            if memo[i][j] != -1:
                return memo[i][j]

            if word1[i] == word2[j]:
                return dp(i-1, j-1)

            memo[i][j] = min(dp(i-1, j) + 1,  # 删除
                           dp(i-1, j-1) + 1,  # 替换
                           dp(i, j-1) + 1  # 插入
                           )
            return memo[i][j]

        return dp(len(word1)-1, len(word2)-1)




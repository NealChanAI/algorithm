# -*- coding: utf-8 -*-
# ===============================================================
#

#
# ===============================================================


class Solution:
    def maximalSquare(self, matrix):
        """
        dp
        :param matrix:
        :return:
        """
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        # base case
        for i in range(m):  # 第一列
            dp[i][0] = int(matrix[i][0])

        for j in range(n):  # 第一行
            dp[0][j] = int(matrix[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    continue

                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dp[i][j])
        return res ** 2



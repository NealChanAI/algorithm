# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/18 01:25
#    @Description   : 62. 不同路径
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = 0
        self.memo = []

    def uniquePaths(self, m, n):
        """"""

        self.memo = [[0] * n for _ in range(m)]

        def dp(i, j):
            if i < 0 or j < 0:
                return 0

            if i == 0 and j == 0:
                return 1

            if self.memo[i][j] != 0:
                return self.memo[i][j]

            self.memo[i][j] = dp(i-1, j) + dp(i, j-1)
            return self.memo[i][j]

        return dp(m-1, n-1)


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))

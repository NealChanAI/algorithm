# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 22:05
#    @Description   : 
#
# ===============================================================


class Solution:
    def uniquePaths(self, m, n):
        """
        自顶项下动态规划
            1. 动态规划子函数定义：返回抵达i, j表格的所有路径条数
            2. base case:
                a. i < 0 or j < 0: 0条
                b. i = 0 and j = 0: 1条
            3. 使用memo二维数组避免重复计算
        :param m:
        :param n:
        :return:
        """

        memo = [[-1] * n for _ in range(m)]

        def dp(i, j):
            # base case
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1

            # 避免重复计算
            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = dp(i - 1, j) + dp(i, j - 1)
            return memo[i][j]

        return dp(m - 1, n - 1)


if __name__ == '__main__':
    m, n = 7, 3
    print(Solution().uniquePaths(m, n))

# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 21:36
#    @Description   : 
#
# ===============================================================


class Solution:
    def minPathSum(self, grid):
        """
        动态数组，自顶向下：
            1. 动态子函数定义：返回到达grid[i][j]所需的最小步数
            2. base case: i < 0 or j < 0, 返回float('inf')
            3. 可使用memo二维数组记录结果，避免重复计算
        :param grid:
        :return:
        """

        # 非空判断
        if not grid:
            return

        m, n = len(grid), len(grid[0])
        memo = [[-1] * n for _ in range(m)]

        def dp(grid, i, j):
            # base case
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                memo[i][j] = grid[0][0]
                return memo[i][j]

            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = min(dp(grid, i-1, j), dp(grid, i, j-1)) + grid[i][j]
            return memo[i][j]

        return dp(grid, m-1, n-1)
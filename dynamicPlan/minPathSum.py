# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/2 16:59
#    @Description   : 64. 最小路径和
#
# ===============================================================


class Solution:
    def minPathSum(self, grid):
        """
        dp函数定义：返回到达该元素的最小路径和
        :param grid:
        :return:
        """
        m = len(grid)
        n = len(grid[0])
        memo = [[-1] * n for _ in range(m)]

        def dp(i, j):
            # base case
            if i == 0 and j == 0:
                memo[i][j] = grid[i][j]
                return memo[i][j]
            # 处理边界问题
            if i < 0 or j < 0:
                return float("inf")

            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = min(dp(i-1, j), dp(i, j-1)) + grid[i][j]
            return memo[i][j]

        return dp(len(grid)-1, len(grid[0])-1)


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))

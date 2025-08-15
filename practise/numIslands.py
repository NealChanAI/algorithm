# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/7/25 17:22
#    @Description   : 200. 岛屿数量
#
# ===============================================================


class Solution:
    def numIslands(self, grid):
        """

        :param grid:
        :return:
        """
        # 非空判断
        if not grid:
            return 0


        m = len(grid)
        n = len(grid[0])

        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)

        return res

    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])

        if i < 0 or j < 0 or i >= m or j >= n:
            return

        if grid[i][j] == "0":
            return

        grid[i][j] = "0"

        self.dfs(grid, i - 1, j)
        self.dfs(grid, i - 1, )
        self.dfs(grid, i, j - 1)


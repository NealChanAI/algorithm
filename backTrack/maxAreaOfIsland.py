# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/18 00:25
#    @Description   : 695. 岛屿的最大面积
#
# ===============================================================


class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            # 边界条件处理
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0

            if grid[i][j] == "0":
                return 0

            # 将岛屿淹没
            grid[i][j] = "0"
            return dfs(grid, i-1, j) + dfs(grid, i+1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1) + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res = max(res, dfs(grid, i, j))

        return res

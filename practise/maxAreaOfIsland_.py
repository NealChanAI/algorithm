# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 15:14
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = 0

    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.res = max(self.res, self.dfs(grid, i, j))

        return self.res

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        # 边界条件
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        # 已经是水
        if grid[i][j] == 0:
            return 0

        # 当前为陆地
        grid[i][j] = 0
        return self.dfs(grid, i - 1, j) \
            + self.dfs(grid, i + 1, j) \
            + self.dfs(grid, i, j - 1) \
            + self.dfs(grid, i, j + 1) + 1

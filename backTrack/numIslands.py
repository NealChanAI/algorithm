# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/18 00:12
#    @Description   : 200. 岛屿数量
#
# ===============================================================


class Sollution:
    def __init__(self):
        self.res = 0

    def numIslands(self, grid):
        if not grid:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.res += 1
                    self.dfs(grid, i, j)

        return self.res


    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])

        # 边界条件
        if i < 0 or j < 0 or i >= m or j >= n:
            return

        # 如果已经被淹了
        if grid[i][j] == "0":
            return

        # 将grid[i][j]淹没
        grid[i][j] = "0"

        # 将上下左右淹没
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/14 16:56
#    @Description   : 
#
# ===============================================================


"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
"""


class Solution:
    def numIslands(self, grid):
        """
        dfs
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    # 将上下左右都淹没
                    self.dfs(grid, i, j)

        return res

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        # 边界条件
        if i < 0 or j < 0 or i >= m or j >= n:
            return

        if grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)


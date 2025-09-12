# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 17:39
#    @Description   : #695
#
# ===============================================================


"""
给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        dfs
        """
        if not grid:
            return

        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, self._helper(grid, i, j))

        return res

    def _helper(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if grid[i][j] == 0:
            return 0

        grid[i][j] = 0

        return 1 + self._helper(grid, i+1, j) + self._helper(grid, i-1, j) + \
            self._helper(grid, i, j-1) + self._helper(grid, i, j+1)

# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 17:18
#    @Description   : #200
#
# ===============================================================


"""
输入一个二维数组 grid，其中只包含 0 或者 1，0 代表海水，1 代表陆地，且假设该矩阵四周都是被海水包围着的。

我们说连成片的陆地形成岛屿，那么请你写一个算法，计算这个矩阵 grid 中岛屿的个数
"""


class Solution:
    def num_islands(self, grid):
        """

        """
        if not grid:
            return

        res = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):

                if grid[i][j] == '1':
                    res +=1

                    self.num_islands_helper(grid, i, j, m, n)


    def num_islands_helper(self, grid, i, j, m, n):
        # base case

        if i < 0 or j < 0 or i >= m or j >= n:
            return
        if grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.num_islands_helper(grid, i - 1, j, m, n)
        self.num_islands_helper(grid, i + 1, j, m, n)
        self.num_islands_helper(grid, i, j - 1, m, n)
        self.num_islands_helper(grid, i, j + 1, m, n)

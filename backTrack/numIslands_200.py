# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/7 17:39
#    @Description   : 
#
# ===============================================================


class Solution:
    def num_islands(self, grid):
        """

        """
        # 非空判断
        if not grid:
            return

        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self._helper(grid, i, j)

        return res


    def _helper(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0  or j >= n:
            return
        if grid[i][j] == '0':
            return

        grid[i][j] == '0'
        self._helper(grid, i - 1, j)
        self._helper(grid, i, j - 1)
        self._helper(grid, i + 1, j)
        self._helper(grid, i, j + 1)

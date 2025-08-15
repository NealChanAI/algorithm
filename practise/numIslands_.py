# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 15:03
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = 0

    def numIslands(self, grid):
        """
        双层for循环遍历，如果是1的话，结果加一，并将上下左右的陆地淹没
        :param grid:
        :return:
        """

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.res += 1
                    self.dfs(grid, i, j)

        return self.res

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])

        # 边界条件处理
        if i < 0 or i >= m or j < 0 or j >= n:
            return

        # 若当前位置为水，则跳过
        if grid[i][j] == '0':
            return

        # 若当前为陆地，则将当前位置淹掉，且将当前位置的上下左右四个方向都淹掉
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
        return







"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
"""


class Solution:
    def __init__(self):
        self.memo = []

    def minPathSum(self, grid):
        """
        dp[i][j]表示走到grid[i][j]的最短路径
        """
        m, n = len(grid), len(grid[0])
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(grid, m-1, n-1)

    def dp(self, grid, i, j):
        # base case
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float('inf')

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        self.memo[i][j] = grid[i][j] + min(self.dp(grid, i-1, j), self.dp(grid, i, j-1))

        return self.memo[i][j]


if __name__ == '__main__':
    a = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    res = a.minPathSum(grid)
    print(res)

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
"""


class Solution:
    def __init__(self):
        self.memo = []

    def uniquePaths(self, m, n):
        """
        dp[i][j]定义：走到grid[i][j]的所有路径
        """
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(m, n, 0, 0)

    def dp(self, m, n, i, j):
        # base case
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        self.memo[i][j] = self.dp(m, n, i + 1, j) + self.dp(m, n, i, j + 1)

        return self.memo[i][j]


if __name__ == '__main__':
    a = Solution()
    m, n = 3, 2
    print(a.uniquePaths(m, n))


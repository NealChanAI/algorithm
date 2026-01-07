# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026/1/7 21:02
#    @Description   : 
#
# ===============================================================


"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。



示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
示例 2：


输入：matrix = [["0","1"],["1","0"]]
输出：1
示例 3：

输入：matrix = [["0"]]
输出：0
"""


class Solution:
    def __init__(self):
        self.memo = []

    def maximalSquare(self, matrix):
        """
        定义dp数组
            dp[i][j]代表以matrix[i][j]为正方形右下角的最大边长
        备忘录
        """

        m, n = len(matrix), len(matrix[0])
        self.memo = [[-1] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    tmp = self._dfs(matrix, i, j)
                    res = max(res, tmp * tmp)
        return res

    def _dfs(self, matrix, i, j):
        # base case
        if i < 0 or j < 0:
            return 0

        if matrix[i][j] == '0':
            self.memo[i][j] = 0
            return 0

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        self.memo[i][j] = min(self._dfs(matrix, i - 1, j)
                ,self._dfs(matrix, i - 1, j - 1)
                ,self._dfs(matrix, i, j - 1)) + 1
        return self.memo[i][j]


if __name__ == '__main__':
    a = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]

    # matrix = [["0", "1"], ["1", "0"]]

    print(a.maximalSquare(matrix))



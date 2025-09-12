# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-01 20:36
#    @Description   : #54
#
# ===============================================================


"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        维护四个边界
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m-1, 0, n-1
        res = []

        while len(res) < m*n:
            # up
            if up <= down:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1

            # right
            if left <= right:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1

            # down
            if up <= down:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1

            # left
            if left <= right:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res



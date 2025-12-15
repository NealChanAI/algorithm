# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-15 16:04
#    @Description   : 
#
# ===============================================================


"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""


class Solution:
    def spiralOrder(self, matrix):
        """维护上下左右四个边界"""

        if not matrix:
            return []

        res = []

        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while len(res) < len(matrix) * len(matrix[0]):
            # 上
            if up <= down:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1

            # 右
            if left <= right:
                for i in range(up, down+1):
                    res.append(matrix[i][right])

                right -= 1

            # 下
            if up <= down:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])

                down -= 1

            # 左
            if left <= right:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])

                left += 1

        return res


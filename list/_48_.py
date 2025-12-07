# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/7 21:10
#    @Description   : 
#
# ===============================================================


"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""

class Solution:
    def rotate(self, matrix):
        """
        1. 先沿着斜对角线将矩阵进行旋转
        2. 再沿着每一行对元素进行反转
        """
        if not matrix:
            return

        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for k in range(n):
            i, j = 0, n - 1
            while i < j:
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
                i += 1
                j -= 1



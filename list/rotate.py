# -*- coding: utf-8 -*-
# ===============================================================

#    @Description   : 48. 旋转图像
#
# ===============================================================

class Solution:
    def rotate(self, matrix):
        """
        思路：
            1. 先将图像用斜对角线进行旋转
            2. 再对每一行进行翻转
        :param matrix:
        :return:
        """
        # 非空判断
        if not matrix:
            return

        # 将matrix沿着对角线进行翻转
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # 将矩阵按行进行翻转
        for i in range(len(matrix)):
            l, r = 0, len(matrix) - 1
            while l < r:
                tmp = matrix[i][l]
                matrix[i][l] = matrix[i][r]
                matrix[i][r] = tmp
                l += 1
                r -= 1
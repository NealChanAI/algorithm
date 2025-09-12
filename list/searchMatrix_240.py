# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-02 11:19
#    @Description   : #240
#
# ===============================================================


"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        从右上角开始搜索
        """
        m, n = len(matrix), len(matrix[0])
        # 从右上角开始搜索
        i, j = 0, n-1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False

# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 08:44
#    @Description   : 
#
# ===============================================================


class Solution:
    def searchMatrix(self, matrix, target):
        """
        从右上角开始遍历，根据与target的大小比较，决定是向下遍历还是向左
        :param matrix:
        :param target:
        :return:
        """
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])

        i, j = 0, n - 1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True

            #
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False
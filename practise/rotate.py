# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 09:05
#    @Description   : 
#
# ===============================================================


class Solution:
    def rotate(self, matrix):
        """
        1. 先将矩阵沿对角线翻转
        2. 对每一行进行翻转
        :param matrix:
        :return:
        """

        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])

        # 将矩阵沿对角线翻转
        for i in range(m):
            for j in range(i, n):
                try:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                except Exception as e:
                    print(i)
                    print(j)
                    raise e

        # 对每一行进行翻转
        for row in matrix:
            for i in range(len(row) // 2):
                row[i], row[len(row)-1-i] = row[len(row)-1-i], row[i]

        return matrix


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))

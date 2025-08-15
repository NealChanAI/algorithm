# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 09:29
#    @Description   : 
#
# ===============================================================


class Solution:
    def spiralOrder(self, matrix):
        """
        螺旋矩阵
        :param matrix:
        :return:
        """
        if not matrix:
            return

        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        res = []
        while len(res) < len(matrix) * len(matrix[0]):
            # 向右遍历
            if up <= down:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1

            # 向下遍历
            if left <= right:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1

            # 向左遍历
            if up <= down:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1

            # 向上遍历
            if left <= right:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res

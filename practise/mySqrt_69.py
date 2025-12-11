# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-11 15:45
#    @Description   : 
#
# ===============================================================


"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        二分法
        :param x:
        :return:
        """
        low, high = 0, x
        res = -1
        while low <= high:
            mid = low + (high - low) // 2
            tmp = mid * mid
            if tmp > x:
                high = mid - 1
            elif tmp < x:
                res = mid
                low = mid + 1
            else:
                return mid
        return res
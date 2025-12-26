# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-25 10:14
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
        双指针
        """

        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            dot = mid * mid
            if dot == x:
                return mid
            elif dot > x:
                r = mid - 1
            else:
                l = mid + 1

        return r


if __name__ == '__main__':
    x = 5
    a = Solution()
    print(a.mySqrt(x))

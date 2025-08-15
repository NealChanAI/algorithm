# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


class Solution:
    def mySqrt(self, x):
        """
        二分法
            1. 找到mid
            2. 判断mid平方与x的大小：
                a. 相等：返回结果
                b. 大于：right = mid - 1
                c. 小于：left = mid + 1
        :param x:
        :return:
        """
        if x < 0:
            return

        l, r = 0, x
        res = -1
        while l < r:
            mid = l + (r - l) // 2
            product = mid * mid
            if product == x:
                return mid
            elif product > x:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        return res

    def _mySqrt(self, x):
        l, r = 0, x
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            product = mid * mid
            if product == x:
                return mid
            elif product > x:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        return res

if __name__ == '__main__':
    # print(Solution().mySqrt(8))
    print(Solution()._mySqrt(8))

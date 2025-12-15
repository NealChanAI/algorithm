# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-15 17:10
#    @Description   : 
#
# ===============================================================


"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution:
    def addStrings(self, nums1, nums2):
        """
        双指针
        """
        if not nums1 and not nums2:
            return

        p1, p2 = len(nums1) - 1, len(nums2) - 1

        res = ''
        tmp = 0
        while p1 >= 0 or p2 >= 0:
            _d1 = int(nums1[p1]) if p1 >= 0 else 0
            _d2 = int(nums2[p2]) if p2 >= 0 else 0
            sum = _d1 + _d2 + tmp
            tmp = sum // 10
            c = sum % 10
            res = str(c) + res

            p1 -= 1
            p2 -= 1

        if tmp != 0:
            res = str(tmp) + res

        return res

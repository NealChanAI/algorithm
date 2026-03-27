# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 12:49
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
        使用进位变量
        """
        res = ''
        p1, p2 = len(nums1) - 1, len(nums2) - 1
        store = 0

        while p1 >= 0 or p2 >= 0:
            n1 = nums1[p1] if p1 >= 0 else 0
            n2 = nums2[p2] if p2 >= 0 else 0

            _sum = int(n1) + int(n2) + store
            yu = _sum % 10
            store = _sum // 10
            res = str(yu) + res

        if store:
            res = str(store) + res

        return res

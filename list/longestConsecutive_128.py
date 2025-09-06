# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 15:50
#    @Description   : #128
#
# ===============================================================


"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""


class Solution:
    def longest_consecutive(self, nums):
        if not nums:
            return

        set_nums = set(nums)
        res = 0

        for num in set_nums:
            # 若不是第一个则跳过
            if num - 1 in set_nums:
                continue

            cur_num = num
            cur_len = 1

            while cur_num+1 in set_nums:
                cur_len += 1
                cur_num += 1

            res = max(res, cur_len)

        return res

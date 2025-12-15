# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/14 18:05
#    @Description   : 
#
# ===============================================================


"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
"""


class Solution:
    def twoSum(self, nums, target):
        """
        1. 遍历
        2. 字典
        """
        d = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in d:
                return [d[need], i]

            d[nums[i]] = i

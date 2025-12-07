# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/7 21:41
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
        使用字典的方式处理,key为具体值，value为索引号
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return

        _dic = dict()

        for i, num in enumerate(nums):
            if target - num in _dic:
                return [_dic[target - nums[i]], i]
            _dic[nums[i]] = i

        return



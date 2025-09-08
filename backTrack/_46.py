# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-08 14:07
#    @Description   : 
#
# ===============================================================


"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
"""


class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.used = []

    def permute(self, nums):
        if not nums:
            return

        self.used = [False] * len(nums)

        def _helper(nums):
            # 更新结果
            if len(self.path) == len(nums):
                self.res.append(self.path.copy)

            for i in range(len(nums)):
                if self.used[i]:
                    continue

                self.path.append(nums[i])
                nums[i] = True
                _helper(nums)
                self.path.pop()
                nums[i] = False

        _helper(nums)
        return self.res
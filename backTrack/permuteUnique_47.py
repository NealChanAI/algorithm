# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 16:53
#    @Description   : #47
#
# ===============================================================


"""
给你输入一个可包含重复数字的序列 nums，请你写一个算法，返回所有可能的全排列
"""


class Solution:
    def __init__(self):
        self.res = []
        self.used = []
        self.path = []

    def permute_unique(self, nums):
        """

        """
        if not nums:
            return

        nums.sort()
        self.used = [False] * len(nums)

        self.back_track(nums)
        return self.res

    def back_track(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue

            if i > 0 and nums[i] == nums[i-1] and not self.used[i-1]:
                continue

            self.path.append(nums[i])
            self.used[i] = True
            self.back_track(nums)
            self.used[i] = False
            self.path.pop()





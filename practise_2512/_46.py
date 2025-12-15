# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/14 18:11
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
        """
        bachTrack
        """

        if not nums:
            return self.res

        self.used = [False] * len(nums)

        self.back_track(nums)

        return self.res

    def back_track(self, nums):
        # base case
        if len(self.path) == len(nums):
            self.res.append(self.path.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue

            self.used[i] = True
            self.path.append(nums[i])
            self.back_track(nums)
            self.path.pop()
            self.used[i] = False

# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 16:12
#    @Description   : #46
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
            return []

        self.used = [False] * len(nums)

        def back_track(nums):
            # 更新结果
            if len(self.path) == len(nums):
                self.res.append(self.path.copy())
                return

            for i in range(len(nums)):
                # 排除不合法的选择
                if not self.used[i]:
                    continue

                self.used[i] = True
                self.path.append(nums[i])

                back_track(nums)

                self.used[i] = False
                self.path.pop()

        back_track(nums)

        return self.res





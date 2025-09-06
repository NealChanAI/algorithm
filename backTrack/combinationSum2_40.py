# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 16:47
#    @Description   : #40
#
# ===============================================================


"""
给你输入 candidates 和一个目标和 target，从 candidates 中找出中所有和为 target 的组合。

candidates 可能存在重复元素，且其中的每个数字最多只能使用一次。
"""


class Solution:
    def __init__(self):
        self.res = []
        self.target_sum = 0
        self.path = []

    def combination_sum2(self, nums, target):
        """
        回溯算法
        """
        if not nums:
            return self.res

        nums.sort()
        self.back_track(nums, 0, target)

    def back_track(self, nums, start, target):
        # 更新结果
        if self.target_sum == target:
            self.res.append(self.path.copy())
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.path.append(nums[i])
            self.target_sum += nums[i]

            self.back_track(nums, i+1, target)

            self.path.pop()
            self.target_sum -= nums[i]


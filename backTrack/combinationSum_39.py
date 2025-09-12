# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 17:03
#    @Description   : #39
#
# ===============================================================


"""
给你一个无重复元素的整数数组 candidates 和一个目标和 target，
找出 candidates 中可以使数字和为目标数 target 的所有组合。candidates 中的每个数字可以无限制重复被选取。
"""


class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.target_sum = 0

    def combinationSum(self, nums, target):
        if not nums:
            return self.res

        self.back_track(nums, 0, target)
        return self.res

    def back_track(self, nums, start, target):
        if self.target_sum == target:
            self.res.append(self.path.copy())
            return
        if self.target_sum > target:
            return

        for i in range(start, len(nums)):
            self.target_sum += nums[i]
            self.path.append(nums[i])
            self.back_track(nums, i, target)
            self.target_sum -= nums[i]
            self.path.pop()

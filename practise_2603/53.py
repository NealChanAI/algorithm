# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 11:51
#    @Description   : 
#
# ===============================================================


"""
给你输入一个整数数组 nums，请你找在其中找一个和最大的子数组，返回这个子数组的和。
"""


class Solution:
    def maxSubArray(self, nums):
        """
        定义dp数组: dp[i]代表以nums[i]为结尾的最大数
        """

        dp = [nums[0]] * len(nums)
        res = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            res = max(res, dp[i])

        return res

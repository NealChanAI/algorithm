# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/12 21:59
#    @Description   : 
#
# ===============================================================


"""
给你输入一个整数数组 nums，请你找在其中找一个和最大的子数组，返回这个子数组的和。
"""


class Solution:
    def maxSubArray(self, nums):
        """定义dp数组
        dp[i]的定义为以nums[i]为结尾的最大数值
        """
        if not nums:
            return

        res = nums[0]
        dp = [0] * len(nums)

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            res = max(dp[i], res)

        return res

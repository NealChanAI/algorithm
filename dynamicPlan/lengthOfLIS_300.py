# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/7 19:25
#    @Description   : #300
#
# ===============================================================


"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
"""


class Solution:
    def length_of_lis(self, nums):
        """
        子问题定义：以数组[i]为结尾的最长子序列
        """
        if not nums:
            return

        dp = [1] * len(nums)
        res = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])

        return res


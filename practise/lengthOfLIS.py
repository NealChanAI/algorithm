# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 21:37
#    @Description   : 
#
# ===============================================================


class Solution:
    def lengthOfLIS(self, nums):
        """最长递增子序列"""
        # 非空判断
        if not nums:
            return

        # 定义dp数组
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        res = 0
        for i in dp:
            res = max(res, i)

        return res


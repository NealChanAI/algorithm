# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/2 12:41
#    @Description   : 
#
# ===============================================================


class Solution:
    def lengthOfLIS(self, nums):
        """
        自底向上, 定义dp table
        dp table：dp[i]代表以nums[i]为最大值，最长的子序列的长度
        base case: dp[0] = 1
        状态转移：往左边找，取
        :param nums:
        :return:
        """
        if not nums:
            return 0

        dp = [1] * len(nums)
        res = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])

        return res




# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/2 12:57
#    @Description   : 
#
# ===============================================================


class Solution:
    def maxSubArray(self, nums):
        """
        dp数组：dp[i]代表以nums[i]为结尾的最大子数组和
        base case: dp[0] = nums[0]
        状态转移：自成一个，或与dp[i-1]相加，两者取较大值
        :param nums:
        :return:
        """
        if not nums:
            return 0

        dp = nums[0] * len(nums)

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])

        res = float("-inf")
        for j in dp:
            res = max(res, j)

        return res



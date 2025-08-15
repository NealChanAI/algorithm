# -*- coding: utf-8 -*-
# ===============================================================
#
# ===============================================================


class Solution:
    def rob(self, nums):
        """
        dp：
            dp[i]表示在位置i所能抢到的最多的钱
            base case:
        :param nums:
        :return:
        """

        memo = [-1] * len(nums)

        def dp(nums, start):
            # base case
            if start >= len(nums):
                return 0

            if memo[start] != -1:
                return memo[start]

            memo[start] = max(nums[start] + dp(nums, start+2),
                        dp(nums, start+1))

            return memo[start]

        return dp(nums, 0)

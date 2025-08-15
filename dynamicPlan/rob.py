# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/2 18:11
#    @Description   : 198. 打家劫舍
#
# ===============================================================


class Solution:
    def rob(self, nums):
        """
        dp函数定义：返回位置i能抢到的最多的钱
        :param nums:
        :return:
        """

        if not nums:
            return 0

        memo = [-1] * len(nums)

        def dp(nums, start):
            # base case
            if start >= len(nums):
                return 0

            if memo[start] != -1:
                return memo[start]

            memo[start] = max(nums[start] + dp(nums, start + 2),
                      dp(nums, start + 1)
                      )
            return memo[start]

        return dp(nums, 0)
# -*- coding: utf-8 -*-
# ===============================================================
#

#
# ===============================================================


class Solution:
    def maxSubArray(self, nums):
        """
        dp数组定义
        :param nums:
        :return:
        """
        # 非空判断
        if not nums:
            return

        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])

        res = float('-inf')
        for i in dp:
            res = max(res, i)

        return res



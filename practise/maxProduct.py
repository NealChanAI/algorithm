# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Description   : 
#
# ===============================================================


class Solution:
    def maxProduct(self, nums):
        """
        dp1: dp1[i]表示以nums[i]为结尾的最大乘积
        dp2: dp2[i]表示以nums[i]为结尾的最小乘积
        :param nums:
        :return:
        """

        if not nums:
            return

        # 定义两个数组
        dp1 = [nums[0]] * len(nums)
        dp2 = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            dp1[i] = max(nums[i],
                         nums[i] * dp1[i-1],
                         nums[i] * dp2[i-1])

            dp2[i] = min(nums[i],
                         nums[i] * dp2[i-1])

        res = float('-inf')
        for e in dp1:
            res = max(res, e)

        return res
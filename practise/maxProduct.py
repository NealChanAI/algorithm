# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Description   : 
#
# ===============================================================


"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

请注意，一个只包含一个元素的数组的乘积是这个元素的值。
"""

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
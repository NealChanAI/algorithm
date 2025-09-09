# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/9 19:01
#    @Description   : 
#
# ===============================================================


"""
给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


class Solution:
    def max_subarray_sum(self, nums):
        """
        1. 非空判断
        2. 定义dp数组：dp[i]为以nums[i]为结尾的最大子数组和
        3. 取当前值或当前值+dp[i-1]的较大值
        """
        if not nums:
            return

        dp = [nums[0]] * len(nums)
        res = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            res = max(res, dp[i])

        return res


if __name__ == '__main__':
    nums = [-1, 2, 3, -4, 5]
    res = Solution().max_subarray_sum(nums)
    print(res)

# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-08 11:01
#    @Description   : 
#
# ===============================================================


"""
给你输入一个整数数组 nums，请你找在其中找一个和最大的子数组，返回这个子数组的和。
"""


class Solution:
    def max_sub_array(self, nums):
        if not nums:
            return

        dp = [nums[0]] * len(nums)
        res = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            res = max(dp[i], res)

        return res


if __name__ == '__main__':
    nums = [5,4,-1,7,8]
    res = Solution().max_sub_array(nums)
    print(res)
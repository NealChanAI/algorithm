# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/7 21:04
#    @Description   : #53
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
        res = nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            res = max(res, dp[i])

        return res


if __name__ == '__main__':
    nums = [5,4,-1,7,8]
    res = Solution().max_sub_array(nums)
    print(res)
# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026/1/4 21:52
#    @Description   : 
#
# ===============================================================


"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

请注意，一个只包含一个元素的数组的乘积是这个元素的值。



示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""


class Solution:
    def maxProduct(self, nums):
        """
        定义两个dp数组
            dp1[i]代表以nums[i]为结尾的最大非空连续子数组
            dp2[i]代表以nums[i]为结尾的最小非空连续子数组
        """
        dp1 = [nums[0]] * len(nums)
        dp2 = [nums[0]] * len(nums)
        res = nums[0]

        for i in range(1, len(nums)):
            dp1[i] = max(max(nums[i], dp1[i-1] * nums[i]), dp2[i-1] * nums[i])
            dp2[i] = min(min(nums[i], dp1[i-1] * nums[i]), dp2[i-1] * nums[i])

            res = max(res, dp1[i])

        return res


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    a = Solution()
    print(a.maxProduct(nums))

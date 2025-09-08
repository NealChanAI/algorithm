# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-08 10:41
#    @Description   : 
#
# ===============================================================


"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
"""

class Solution:
    def twoSum(self, nums, start, end, target):
        if start >= end:
            return
        res = []
        l, r = start, end
        while l < r:
            _sum = nums[l] + nums[r]
            if _sum == target:
                res.append([nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                l += 1
                while l < r and nums[r-1] == nums[r]:
                    r -= 1
                r -= 1
            elif _sum > target:
                r -= 1
            else:
                l += 1
        return res

    def threeSum(self, nums):
        if not nums:
            return

        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 1 and nums[i] == nums[i-1]:
                continue
            two_sum_res = self.twoSum(nums, i + 1, len(nums) - 1, -nums[i])
            if two_sum_res:
                for s, e in two_sum_res:
                    res.append([nums[i], s, e])

        return res

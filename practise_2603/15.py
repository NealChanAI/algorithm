# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 11:15
#    @Description   : 
#
# ===============================================================


"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
"""


class Solution:
    def threeSum(self, nums):
        """使用two sum的方式来处理, 需注意重复数值"""
        if not nums:
            return

        res = []

        nums.sort()

        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            tmp_res = self._twoSum(nums, i+1, i+2, -nums[i])
            if tmp_res:
                for e in tmp_res:
                    res.append([nums[i], e[0], e[1]])

        return res

    def _twoSum(self, nums, start, end, target):
        """two Sum实现: 双指针"""
        res = []

        l, r = start, end

        while l < r:
            _sum = nums[l] + nums[r]
            if _sum > target:
                r -= 1
            elif _sum < target:
                l += 1
            else:
                res.append([nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                r -= 1

        return res





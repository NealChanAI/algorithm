# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/12 21:44
#    @Description   : 
#
# ===============================================================


"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
"""


class Solution:
    def threeSum(self, nums):
        """
        1. two sum
        """

        if not nums:
            return

        res = []
        nums.sort()

        for i in range(len(nums)-2):
            # 跳过重复的
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tmp_res = self.twoSum(nums, i+1, -nums[i])
            if tmp_res:
                for j, k in tmp_res:
                    res.append([nums[i], j, k])
        return res

    def twoSum(self, nums, start, target):
        """
        two sum实现
        左右指针
        """
        _res = []
        l, r = start, len(nums)-1
        while l < r:
            tmp = nums[l] + nums[r]
            if tmp > target:
                r -= 1
            elif tmp < target:
                l += 1
            else:
                _res.append([nums[l], nums[r]])
                while l < r and nums[l+1] == nums[l]:
                    l += 1
                l += 1

                while l < r and nums[r-1] == nums[r]:
                    r -= 1
                r -= 1
        return _res

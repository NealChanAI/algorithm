# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-01 16:55
#    @Description   : #15
#
# ===============================================================


"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
"""

class Solution:
    def two_sum(self, nums, start, end, target):
        res = []
        left, right = start, end
        while left < right:
            _sum = nums[left] + nums[right]
            if _sum > target:
                right -= 1
            elif _sum < target:
                left += 1
            elif _sum == target:
                res.append([left, right])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
        return res

    def three_sum(self, nums):
        """
        1. 非空判断
        2. 转换为two sum问题
        """
        # 非空判断
        if not nums:
            return

        res = []

        # 将nums进行排序
        nums.sort()
        for i in range(0, len(nums)-2):
            # 避免重复
            if i > 0 and nums[i] == nums[i-1]:
                continue

            two_sum_res = self.two_sum(nums, i+1, len(nums)-1, -nums[i])
            if two_sum_res:
                res.append([i, two_sum_res[0], two_sum_res[1]])

        return

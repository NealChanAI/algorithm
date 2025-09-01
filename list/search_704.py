# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-01 16:31
#    @Description   : #704
#
# ===============================================================


"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果 target 存在返回下标，否则返回 -1。
"""

class Solution:
    def search(self, nums, target):
        """
        1. 非空判断
        2. 二分查找
        """
        # 非空判断
        if not nums:
            return

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return  -1
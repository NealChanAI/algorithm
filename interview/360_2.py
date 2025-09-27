# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/16 19:12
#    @Description   : 
#
# ===============================================================


"""
二维数组，0和1，找出所有被1包围的0，o(n^2)

升序数组，有重复数字，最左边
"""


class Solution:
    def __init__(self):
        pass

    def left_side(nums, target):
        """
        1. 非空判断
        2. 双指针
        """
        if not nums:
            return

        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if nums[left] != target:
            return -1

        return left






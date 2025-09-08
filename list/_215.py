# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-08 10:06
#    @Description   : 
#
# ===============================================================


"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""


class Solution:
    def __init__(self):
        self.res = None

    def parition(self, nums, start, end, k):

        if start > end:
            return
        pivot = nums[start]
        l, r = start, end

        while l < r:
            while l < r and nums[l] <= pivot:
                l += 1
            nums[r] = nums[l]
            while l < r and nums[r] > pivot:
                r -= 1
            nums[l] = nums[r]

        nums[l] = pivot

        if l == len(nums) - k:
            return pivot
        elif l > len(nums) - k:
            self.parition(nums, start, l - 1, k)
        else:
            self.parition(nums, l + 1, end, k)

    def find_kth_largest(self, nums, k):
        """
        快速排序
        """
        if not nums or k <= 0:
            return

        return self.parition(nums, 0, len(nums) - 1, k)



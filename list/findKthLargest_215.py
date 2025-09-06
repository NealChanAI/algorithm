# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 15:18
#    @Description   : #215
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

    def find_kth_largest(self, nums, k):
        """
        快速排序
        """
        if not nums:
            return

        def find_kth_largest_helper(nums, start, end):
            if start > end:
                return

            low, high = start, end
            pivot = nums[low]

            while low < high:
                while low < high and nums[low] <= pivot:
                    low += 1
                nums[high] = nums[low]

                while low < high and nums[high] > pivot:
                    high -= 1
                nums[low] = nums[high]

            nums[low] = pivot

            if low == len(nums) - k:
                self.res = pivot
                return
            elif low < len(nums) - k:
                find_kth_largest_helper(nums, low+1, end)
            else:
                find_kth_largest_helper(nums, start, low)

        find_kth_largest_helper(nums, 0, len(nums)-1)

        return self.res

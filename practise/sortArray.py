# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 12:27
#    @Description   : 
#
# ===============================================================


import random

class Solution:
    def sortArray(self, nums):
        """

        :param nums:
        :return:
        """
        if not nums:
            return

        def quick_sort_helper(nums, start, end):
            if start >= end:
                return
            left, right = start, end
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] < pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            quick_sort_helper(nums, start, left - 1)
            quick_sort_helper(nums, left + 1, end)

        rnd = random.Random()
        for i in range(len(nums)):
            j = rnd.randint(i, len(nums)-1)
            nums[i], nums[j] = nums[j], nums[i]

        quick_sort_helper(nums, 0, len(nums) - 1)
        return nums
# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 11:34
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = float('inf')

    def findKthLargest(self, nums, k):
        """
        quick sort
        :param nums:
        :param k:
        :return:
        """
        def quick_sort(nums, start, end):
            if start > end:
                return

            left, right = start, end
            pivot = nums[left]

            while left < right:
                # 从右往左遍历
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                # 从左往右遍历
                while left and nums[left] < pivot:
                    left += 1
                nums[right] = nums[left]

            # 双指针相遇时
            nums[left] = pivot

            if len(nums) - left == k:
                return pivot
            elif len(nums) - left > k:
                quick_sort(nums, left+1, end)
            else:
                quick_sort(nums, start, left - 1)

        return quick_sort(nums, 0, len(nums) - 1)

# -*- coding: utf-8 -*-
# ===============================================================
#
# ===============================================================


class Solution:
    def findPeakElement(self, nums):
        """
        二分法
        :param nums:
        :return:
        """
        # 合理性判断
        if not nums:
            return

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left

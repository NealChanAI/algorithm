# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/8/17 16:06
#    @Description   : 
#
# ===============================================================


class Solution:
    def search(self, nums, target):
        """
        二分查找
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

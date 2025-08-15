# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 08:27
#    @Description   : 
#
# ===============================================================


class Solution:
    def search(self, nums, target):
        """
        二分搜索法：
            1. 断崖位置：左边的所有元素比右边的所有元素大
            2. 查看mid的大小：
                mid比left大(含相等)：则mid落在左边
                mid比left小：则mid落在右边
        :param nums:
        :param target:
        :return:
        """
        # 非空判断
        if not nums:
            return

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 找到target:
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:  # mid落在左边
                if target >= nums[left] and target < nums[mid]:  # target在左子区间
                    right = mid - 1
                else:  # 其他情况，需要左移动mid，因此调整mid的位置
                    left = mid + 1
            else:  # mid落在右边
                if target > nums[mid] and target <= nums[right]:  # target在右子区间
                    left = mid + 1
                else:
                    right = mid -1
        # 找不到
        return -1
# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 15:40
#    @Description   : 
#
# ===============================================================


class Solution:
    def findPeakElement(self, nums):
        """
        二分查找：
            找到mid
            判断mid和mid+1的大小：
                nums[mid] > nums[mid+1]: 下行，峰值在左边，令right = mid
                nums[mid] < nums[mid+1]: 上行，峰值在左边，令left = mid + 1
        :param nums:
        :return:
        """
        if not nums:
            return

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1

        return left


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().findPeakElement(nums))

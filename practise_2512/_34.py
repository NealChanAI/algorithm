# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-19 17:24
#    @Description   : 
#
# ===============================================================


"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

输入：nums = [5, 7, 7, 8, 8, 10], target = 8
输出：[3, 4]
示例
2：

输入：nums = [5, 7, 7, 8, 8, 10], target = 6
输出：[-1, -1]
示例
3：

输入：nums = [], target = 0
输出：[-1, -1]

"""


class Solution:
    def search_range(self, nums, target):
        """
        非空判断
        左边界
        右边界
        """
        if not nums:
            return [-1, -1]

        return [self.left_bound(nums, target), self.right_bound(nums, target)]

    def left_bound(self, nums, target):
        """搜索左边界"""
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if r < 0 or nums[l] != target:
            return -1

        return l


    def right_bound(self, nums, target):
        """搜索右边界"""
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                l = mid + 1

        if l >= len(nums) or nums[r] != target:
            return -1

        return r


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    nums = [5, 7, 7, 8, 8, 10]
    # target = 6

    a = Solution()
    res = a.search_range(nums, target)
    print(res)

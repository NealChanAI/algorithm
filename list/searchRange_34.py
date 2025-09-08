# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-02 10:50
#    @Description   : #34
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
        分别计算左边界和右边界
        """
        if not nums:
            return

        return [self.left_bound(nums, target), self.right_bound(nums, target)]

    def left_bound(self, nums, target):
        if not nums:
            return

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid - 1

        if left >= len(nums) or nums[left] != target:
            return -1

        return left

    def right_bound(self, nums, target):
        if not nums:
            return

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid + 1

        if right < 0 or nums[right] != target:
            return -1
        return right


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    res = Solution().search_range(nums, target)
    print(res)

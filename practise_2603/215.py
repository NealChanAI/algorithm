# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-02 11:17
#    @Description   : 
#
# ===============================================================


"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""


class Solution:
    def findKthLargest(self, nums, k):
        """quick sort"""

        return self._helper(nums, 0, len(nums)-1, k)

    def _helper(self, nums, start, end, k):
        if start > end:
            return

        pivot = nums[start]
        l, r = start, end

        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]

            while l < r and nums[l] < pivot:
                l += 1
            nums[r] = nums[l]

        nums[l] = pivot

        if len(nums) - l == k:
            return pivot
        elif len(nums) - l > k:
            return self._helper(nums, l+1, end, k)
        else:
            return self._helper(nums, start, l-1, k)


if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 5
    a = Solution()
    print(a.findKthLargest(nums, k))







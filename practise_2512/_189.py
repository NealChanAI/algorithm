# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-01-06 20:18
#    @Description   : 
#
# ===============================================================


"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。



示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
"""


class Solution:
    def rotate(self, nums, k):
        """
        旋转三次
        """
        def _reverse(nums, i, j):
            """旋转指定索引部分的数组"""
            l, r = i, j
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k = k % n
        _reverse(nums, 0, n-1)
        _reverse(nums, 0, k-1)
        _reverse(nums, k, n-1)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    a = Solution()
    a.rotate(nums, k)
    print(nums)


# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-02 10:10
#    @Description   : #560
#
# ===============================================================


"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。
"""

class Solution:
    def subarraySum(self, nums, k):
        """
        1. 前缀和
        2. 字典记录
        """
        if not nums:
            return

        pre_sum = [0] * (len(nums)+1)
        count = {0:1}
        res = 0

        for i, n in enumerate(nums):
            pre_sum[i+1] = nums[i] + pre_sum[i]
            if pre_sum[i+1] not in count:
                count[pre_sum[i+1]] = 0
            count[pre_sum[i + 1]] += 1

            target = k - pre_sum[i+1]
            if target in count:
                res += count[target]

        return res


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2

    nums = [1,2,3]
    k = 3
    res = Solution().subarraySum(nums, k)
    print(res)

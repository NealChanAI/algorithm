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
        """前缀和"""
        pre_sum = [0] * len(nums)
        cnt = dict()
        res = 0
        cnt[0] = 1

        for i in range(0, len(nums)):
            if i == 0:
                pre_sum[i] = nums[i]
            else:
                pre_sum[i] = nums[i] + pre_sum[i - 1]

            need = pre_sum[i] - k
            if need in cnt:
                res += cnt[need]

            if pre_sum[i] not in cnt:
                cnt[pre_sum[i]] = 0
            cnt[pre_sum[i]] += 1

        return res


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2

    nums = [1,2,3]
    k = 3
    res = Solution().subarraySum(nums, k)
    print(res)

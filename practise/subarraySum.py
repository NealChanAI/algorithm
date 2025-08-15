# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


class Solution:
    def subarraySum(self, nums, k):
        """前缀和"""
        pre_sum = [0] * len(nums)
        cnt = dict()
        res = 0

        for i in range(0, len(nums)):
            if i == 0:
                pre_sum[i] = nums[i]
            else:
                pre_sum[i] = nums[i] + pre_sum[i-1]

            need = pre_sum[i] - k
            if need in cnt:
                res += cnt[need]

            if pre_sum[i] not in cnt:
                cnt[pre_sum] = 0
            cnt[pre_sum] += 1

        return res

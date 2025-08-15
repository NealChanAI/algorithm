# -*- coding: utf-8 -*-
# ===============================================================
#

#
# ===============================================================

class Solution:
    def subarray_sum(self, nums, k):

        pre_sum = [0] * (len(nums) + 1)
        count = dict()
        count[0] = 1
        res = 0

        for i in range(1, len(nums)):
            pre_sum[i] = pre_sum[i-1] + nums[i]

            need = pre_sum[i] - k
            if need in count:
                res += count[need]

            if pre_sum[i] not in count:
                count[pre_sum[i]] = 1
            count[pre_sum[i]] += 1

        return res



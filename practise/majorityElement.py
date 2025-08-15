# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/20 09:02
#    @Description   : 
#
# ===============================================================


class Solution:
    def majorityElement(self, nums):
        """多数元素"""
        cnt = dict()

        for num in nums:
            if num not in cnt:
                cnt[num] = 0
            cnt[num] += 1

        for k, v in cnt.items():
            if v > len(nums) / 2:
                return k

        return
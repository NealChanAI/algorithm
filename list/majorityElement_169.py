# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 15:57
#    @Description   : #169
#
# ===============================================================


"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""


class Solution:
    def majority_element(self, nums):
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
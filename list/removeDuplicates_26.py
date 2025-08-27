# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-27 16:56
#    @Description   : #26
#
# ===============================================================


class Solution:
    def remove_duplicates(self, nums):
        """
        1. 非空判断
        2. 快慢指针
        """
        # 非空判断
        if not nums:
            return

        s, f = 0, 0
        while f < len(nums):
            f += 1
            if nums[f] != nums[s]:
                s += 1
                nums[s] = nums[f]

        return s + 1
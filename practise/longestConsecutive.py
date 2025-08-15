# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 21:55
#    @Description   : 
#
# ===============================================================


class Solution:
    def longestConsecutive(self, nums):
        """
        查找子序列的开头第一个元素
        :param nums:
        :return:
        """
        if not nums:
            return 0

        if len(nums) <= 1:
            return len(nums)

        nums = set(nums)

        res = 0

        for num in nums:
            # 非第一个元素
            if num - 1 in nums:
                continue

            cur_num, cur_len = num, 1
            while cur_num + 1 in nums:
                cur_len += 1
                cur_num += 1

            res = max(res, cur_len)

        return res

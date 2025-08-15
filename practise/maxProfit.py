# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/16 20:41
#    @Description   : 
#
# ===============================================================


class Solution:
    def maxProfit(self, nums):
        """

        :param nums:
        :return:
        """
        min_price = nums[0]
        max_profit = 0
        for i in range(1, len(nums)):
            min_price = min(min_price, nums[i])
            max_profit = max(max_profit, nums[i])
        return max_profit
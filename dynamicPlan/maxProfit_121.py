# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-10 16:31
#    @Description   : #121
#
# ===============================================================


"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""


class Solution:
    def maxProfit(self, prices):
        """
        一次交易, 找最小值和最大值
        """
        # 非空判断
        if not prices:
            return

        min_val = float('inf')
        max_profit = 0

        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price-min_val)
        return max_profit

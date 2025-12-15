# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/14 19:29
#    @Description   : 
#
# ===============================================================


"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""


class Solution:
    def maxProfit(self, prices):
        min_val, max_profit = float('inf'), 0

        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price - min_val)

        return max_profit
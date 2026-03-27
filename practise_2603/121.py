# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 12:48
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
        """
        遍历获取价格最低的股票
        """

        max_profit = 0
        low_price = prices[0]

        for price in prices:
            low_price = min(price, low_price)
            max_profit = max(max_profit, price - low_price)

        return max_profit
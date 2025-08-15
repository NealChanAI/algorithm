# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/2 18:56
#    @Description   : 121. 买卖股票的最佳时机
#
# ===============================================================


class Solution:
    def maxProfit(self, prices):
        """
        仅限一次交易
        :param prices:
        :return:
        """
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

    def _maxProfit(self, prices):
        """
        无限次交易：贪心策略，有上涨就买卖，没上涨就不买卖
        :param prices:
        :return:
        """
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                profit += tmp
        return profit



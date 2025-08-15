# -*- coding: utf-8 -*-

# ===============================================================


def maxProfit(prices):
    if not prices:
        return 0

    profit = 0
    for i in range(1, len(prices)):
        tmp = prices[i] - prices[i-1]
        if tmp > 0:
            profit += tmp

    return profit

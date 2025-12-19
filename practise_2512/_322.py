# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-19 17:02
#    @Description   : 
#
# ===============================================================


"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。
"""


class Solution:
    def __init__(self):
        self.res = -1
        self.memo = []

    def coinChange(self, coins, amount):
        self.memo = [-1] * (amount + 1)
        return self.dp(coins, amount)


    def dp(self, coins, amount):
        """
        递归子函数定义: 返回可以抽成总金额所需的最少的硬币个数
        """
        if amount == 0:
            return 0

        if amount < 0:
            return -1

        if self.memo[amount] != -1:
            return self.memo[amount]

        res = float('inf')

        for coin in coins:
            _res = self.dp(coins, amount - coin)
            if _res == -1:
                continue
            res = min(_res + 1, res)

        self.memo[amount] = res

        return res



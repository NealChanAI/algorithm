# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/7 19:12
#    @Description   : #322
#
# ===============================================================


"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。
"""


class Solution:
    def __init__(self):
        self.memo = []

    def dp(self, coins, amount):
        # base case
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        if self.memo[amount] != -1:
            return self.memo[amount]

        res = float('inf')
        for coin in coins:
            need = self.dp(coins, amount - coin)
            if need == -1:
                continue
            res = min(res, 1 + need)

        self.memo[amount] = res if res != float('inf') else -1

        return self.memo[amount]

    def coin_change(self, coins, amount):
        """
        dp数组
        memo
        """
        if not coins or not amount:
            return

        self.memo = [-1] * (amount + 1)

        return self.dp(coins, amount)


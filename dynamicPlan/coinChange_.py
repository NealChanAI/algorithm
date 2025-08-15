# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/2 11:11
#    @Description   : 
#
# ===============================================================


class Solution:
    def coinChange(self, coins, amount):
        """
        递归子函数：返回凑齐amount所需要的最少硬币数
        :param coins:
        :param amount:
        :return:
        """
        memo = [-666] * (amount + 1)

        def dp(coins, amount):
            # base case
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            if memo[amount] != -666:
                return memo[amount]

            res = float("inf")
            for coin in coins:
                need = dp(coins, amount - coin)
                if need == -1:
                    continue
                res = min(res, need + 1)
            memo[amount] = res if res != float("inf") else -1
            return memo[amount]
        return dp(coins, amount)


if __name__ == '__main__':
    coins = [698, 308, 198, 128, 68, 6]
    amount = 1644
    print(Solution().coinChange(coins, amount))

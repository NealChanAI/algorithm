# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 21:23
#    @Description   : 
#
# ===============================================================


class Solution:
    def coinChange(self, coins, amount):
        """
        自顶向下dp:
            1. 动态子函数定义：返回凑齐amount数量所需的最少硬币数量
            2. base case:
                a. amount等于0：返回0
                b. amount小于0：返回-1
            3. 可结合memo数组解决重复计算问题
        :param coins:
        :param amount:
        :return:
        """

        # 非空判断
        if not coins:
            return

        # memo数组
        memo = [-10] * (amount + 1)

        def dp(coins, amount):
            # base case
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            # 判断是否已经计算过
            if memo[amount] != -10:
                return memo[amount]

            # 存储最终结果
            res = float('inf')

            for coin in coins:
                min_need = dp(coins, amount - coin)
                # 无结果
                if min_need == -1:
                    continue
                res = min(res, 1 + min_need)
            memo[amount] = res if res != float('inf') else -1
            return memo[amount]

        return dp(coins, amount)


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    coins = [1]
    amount = 0
    print(Solution().coinChange(coins, amount))





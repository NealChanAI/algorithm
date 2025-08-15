# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/13 17:22
#    @Description   : 
#
# ===============================================================


def coinChange(coins, amount):
    """
    动态规划：
    递归函数定义：返回需要凑齐目标amount所需的最少coin数
    :param coins:
    :param amount:
    :return:
    """
    # 使用备忘录，避免重复查询
    memos = [-666] * (amount + 1)

    def dp_coin(coins, amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if memos[amount] != -666:
            return memos[amount]

        res = float("inf")
        for coin in coins:
            sub_res = dp_coin(coins, amount - coin)
            if sub_res == -1:
                continue
            res = min(res, sub_res + 1)
        memos[amount] = res if res != float("inf") else -1
        return memos[amount]

    return dp_coin(coins, amount)





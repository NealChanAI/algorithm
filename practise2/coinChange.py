

class Solution:
    def coinChange(self, coins, amount):
        return self.dp(coins, amount)

    def dp(self, coins, amount):
        # base case
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        res = float('inf')
        for coin in coins:
            # 计算子问题的结果
            sub_problem = self.dp(coins, amount-coin)
            # 子问题无解则跳过
            if sub_problem == -1:
                continue
            # 在子问题中选择最优解，然后加一
            res = min(res, sub_problem + 1)

        return res if res != float('inf') else -1


class Solution2:
    def __init__(self):
        self.memo = []

    def coinChange(self, coins, amount):
        self.memo = [-666] * (amount + 1)
        # 备忘录初始化位一个不会被取到的特殊值，代表还未被计算
        return self.dp(coins, amount)

    def dp(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        # 查备忘录，防止重复计算
        if self.memo[amount] != -666:
            return self.memo[amount]

        res = float('inf')
        for coin in coins:
            # 计算子问题的结果
            sub_problem = self.dp(coins, amount-coin)

            # 子问题无解则跳过
            if sub_problem == -1:
                continue

            # 在子问题中选择最优解
            res = min(res, sub_problem+1)

        self.memo[amount] = res if res != float('inf') else -1
        return self.memo[amount]


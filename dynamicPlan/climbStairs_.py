# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/2 10:57
#    @Description   : 
#
# ===============================================================


class Solution:
    def climbStairs(self, n):
        """
        自底向上
        定义dp列表
        :param n:
        :return:
        """
        dp = [1] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def _climbStairs(self, n):
        """
        自顶向下

        :param n:
        :return:
        """
        memo = [-666] * (n + 1)

        def _climb_helper(n):
            # base case
            if n == 1 or n == 2:
                return n

            if memo[n] != -666:
                return memo[n]

            memo[n] = _climb_helper(n-1) + _climb_helper(n-2)

            return memo[n]


if __name__ == '__main__':
    print(Solution().climbStairs(4))
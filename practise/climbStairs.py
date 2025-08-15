# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 21:10
#    @Description   : 
#
# ===============================================================


class Solution:
    def climbStairs(self, n):
        """自底向上dp"""
        if n == 1:
            return 1

        dp = [1] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def _helper(self, n):
        """自顶向下"""
        # base case
        if n == 1 or n == 0:
            return 1

        return self._helper(n-1) + self._helper(n-2)


if __name__ == '__main__':
    print(Solution()._helper(3))

# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-19 16:30
#    @Description   : 
#
# ===============================================================


"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""


class Solution:
    def climbStairs(self, n):
        """自底向上"""
        if not n:
            return 0

        dp = [1] * (len(n) + 1)

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n+1]


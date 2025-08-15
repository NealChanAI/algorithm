# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/28 08:45
#    @Description   : 70
#
# ===============================================================


class Solution:
    def climbStairs(self, n):
        dp = [1] * (n+1)

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            # print("i: {}---dp: {} ".format(str(i), str(dp[i])))

        return dp[n]


if __name__ == '__main__':
    Solution().climbStairs(3)

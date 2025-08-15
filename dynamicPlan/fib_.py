# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/13 17:03
#    @Description   : 
#
# ===============================================================


def fib(n):
    """
    递推
    :param n:
    :return:
    """
    if n == 0:
        return 0
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i+1] + dp[i+2]

    return dp[n]


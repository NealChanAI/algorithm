# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/13 16:51
#    @Description   : 
#
# ===============================================================


def fib(n):
    memo = [0] * (n+1)
    return recur(memo, n)


def recur(memo, n):
    """
    带备忘录的递归求解
    递归函数定义：子函数返回n-1, n-2节点值的求和
    :param memo:
    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] != 0:
        return memo[n]
    dp_n_1 = recur(memo, n - 1)
    dp_n_2 = recur(memo, n - 2)

    memo[n] = dp_n_1 + dp_n_2

    return memo[n]

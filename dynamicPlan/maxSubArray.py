# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/13 20:53
#    @Description   : 
#
# ===============================================================


def max_sub_array(nums):
    """
    动态规划，dp定义：dp[i]代表以num[i]为结尾的最大连续子数组和
    base case dp[0] = nums[0]
    状态转移：由dp[k-1]怎么推导出dp[k]
        1. 自成一派
        2. 与上一个结合到一起，变成更大的数
    :param nums:
    :return:
    """
    # 合理性判断
    if not nums or len(nums) == 0:
        return

    # base case
    dp = [nums[0]] * len(nums)
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i-1])

    res = float("-inf")
    for r in dp:
        res = max(res, r)
    return res

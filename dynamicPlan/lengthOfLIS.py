# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/13 20:27
#    @Description   : 
#
# ===============================================================


def lengthOfLIS(nums):
    """
    动态规划：
        dp表定义：dp[i]代表以nums[i]为结尾的最长递增子序列的长度
        base case: dp[0] = 1
        状态转移：dp[j]，从头开始遍历，发现有比nums[j]小的数，则加一，取最大的那个数
    :param nums:
    :return:
    """
    if not nums or len(nums) == 0:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(dp)

    res = 0
    for i in dp:
        res = max(res, i)

    return res


if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    lengthOfLIS(nums)
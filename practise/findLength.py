# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/20 09:41
#    @Description   : 
#
# ===============================================================


class Solution:
    def findLength(self, nums1, nums2):
        m, n = len(nums1), len(nums2)

        res = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])

        return res
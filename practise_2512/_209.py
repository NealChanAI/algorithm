"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
"""


class Solution:
    def minSubArrayLen(self, target, nums):
        """
        slinding window
        """
        res = float('inf')

        l, r = 0, 0
        sum = 0

        while r < len(nums):
            # 扩大窗口
            c = nums[r]
            r += 1

            sum += c

            while sum >= target and l < r:
                # 更新结果
                if r - l < res:
                    res = r - l

                d = nums[l]
                l += 1
                sum -= d

        return res if res != float('inf') else 0



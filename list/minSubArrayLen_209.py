# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-02 10:26
#    @Description   : #209
#
# ===============================================================


"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
"""


class Solution:
    def minSubArrayLen(self, target, nums):
        """
        sliding window
        """
        if not nums:
            return

        res = float('inf')
        l, r = 0, 0
        window = 0

        while r < len(nums):
            # 扩大窗口
            n = nums[r]
            r += 1
            # 更新数据
            window += n

            while window >= target and l <= r:
                # 更新结果
                res = min(res, r-l)

                # 缩小窗口
                d = nums[l]
                l += 1

                window -= d

        return 0 if res == float('inf') else res


if __name__ == '__main__':
    target = 7
    nums = [2,3,1,2,4,3]

    target = 4
    nums = [1,4,4]
    res = Solution().min_subarray_len(target, nums)
    print(res)

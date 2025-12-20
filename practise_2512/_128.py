"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""


class Solution:
    def longestConsecutive(self, nums):
        """
        使用set
        """

        s = set(nums)
        res = 0

        for num in s:  #
            # 排除掉非第一个数
            if num - 1 in s:
                continue

            # 找到了第一个数
            cur = num
            len = 1
            while (cur + 1) in s:
                cur += 1
                len += 1

            res = max(res, len)

        return res




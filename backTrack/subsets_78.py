# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 16:33
#    @Description   : #78
#
# ===============================================================


"""
给你输入一个无重复元素的数组 nums，其中每个元素最多使用一次，请你返回 nums 的所有子集。
"""


class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def subsets(self, nums):
        pass

    def backTrack(self, nums, start):
        self.res.append(self.path.copy())

        for i in range(start, len(nums)):
            self.path.append(nums[i])

            self.backTrack(nums, i+1)

            self.path.pop()

# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-01-05 14:04
#    @Description   : 
#
# ===============================================================


"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""


class Test:
    def __init__(self):
        self.res = []
        self.path = []

    def subsets(self, nums):
        """backtrack"""
        self._back_track(nums, 0)
        return self.res

    def _back_track(self, nums, start):
        # base case
        if start > len(nums):
            return

        self.res.append(self.path.copy())

        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self._back_track(nums, i+1)
            self.path.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Test().subsets(nums))




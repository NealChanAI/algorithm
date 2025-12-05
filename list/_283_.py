# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-05 18:01
#    @Description   : 
#
# ===============================================================


"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""

class Solution:
    def moveZeroes(self, nums):
        """
        1. 非空判断
        2. 双指针
            起始于0索引
            f指针去找非0的, 然后赋值给s, 然后s往前移动
            当f到最后的时候,
        """
        if not nums:
            return

        s, f = 0, 0

        while f < len(nums):
            if nums[f] != 0:
                nums[s] = nums[f]
                s += 1
            f += 1

        for i in range(s, len(nums)):
            nums[i] = 0

        return nums



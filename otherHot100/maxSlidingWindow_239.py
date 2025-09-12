# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-02 15:24
#    @Description   : #239
#
# ===============================================================


"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。
"""


from collections import deque


class MonotonicQueue:
    """
    单调队列
    """
    def __init__(self):
        self.maxq = deque()

    def push(self, val):
        while self.maxq and val > self.maxq[-1]:
            self.maxq.pop()
        self.maxq.append(val)

    def max(self):
        return self.maxq[0]

    def pop(self, n):
        if n == self.maxq[0]:
            self.maxq.popleft()


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return

        res = []

        window = MonotonicQueue()
        for i in range(k-1):
            window.push(nums[i])

        for i in range(k-1, len(nums)):
            window.push(nums[i])
            res.append(window.max())
            window.pop(nums[i-k+1])

        return res




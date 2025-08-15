# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 21:27
#    @Description   : 239. 滑动窗口最大值
#
# ===============================================================


from collections import deque


class MonotationQueue:
    def __init__(self):
        self.maxq = deque()

    def push(self, n):
        while self.maxq and n > self.maxq[-1]:
            self.maxq.pop()
        self.maxq.append(n)

    def pop(self, n):
        if n == self.maxq[0]:
            self.maxq.popleft()

    def max(self):
        return self.maxq[0]


def maxSlidingWindow(nums, k):
    mque = MonotationQueue()
    res = []

    for i in range(len(nums)):
        if i < k - 1:
            mque.push(nums[i])
        else:
            mque.push(nums[i])
            res.append(mque.max())
            mque.pop(nums[i - k + 1])
    return res


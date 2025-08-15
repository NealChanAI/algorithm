# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/8/19 20:14
#    @Description   : 
#
# ===============================================================


class MinStack:
    def __init__(self):
        self.std = []
        self.min = []  # 用于存储当前的最小值

    def push(self, val):
        """推送"""
        self.std.append(val)

        # 不存在
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def top(self):
        return self.std[-1]

    def pop(self):
        self.std.pop()
        self.min.pop()

    def getMin(self):
        return self.min[-1]
# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/8/19 17:18
#    @Description   : 
#
# ===============================================================


class MyQueue:
    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x):
        self.a.append(x)

    def peek(self):
        """返回队头元素"""
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
            return self.b[-1]

    def pop(self):
        """删除队头元素"""
        self.peek()
        self.b.pop()

    def empty(self):
        return not self.a and self.b


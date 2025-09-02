# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-02 15:55
#    @Description   : #155
#
# ===============================================================


"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
"""


class MinStack:
    def __init__(self):
        self.std = []
        self.min_stack = []

    def push(self, val):
        """将元素val推入堆栈"""
        self.str.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            min_val = min(self.min_stack, val)
            self.min_stack.append(min_val)

    def pop(self):
        """删除堆栈顶部的元素"""
        self.str.pop()
        self.min_stack.pop()

    def top(self):
        """获取堆栈顶部的元素"""
        return self.std[-1]

    def getMin(self):
        """获取堆栈中的最小元素"""
        return self.min_stack[-1]

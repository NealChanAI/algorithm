# -*- coding: utf-8 -*-
# ===============================================================
#
# ===============================================================


class MyQueue:
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x):
        self.A.append(x)

    def pop(self):
        peek = self.peek()
        self.B.pop()
        return peek

    def peek(self):
        if self.B:
            return self.B[-1]
        if not self.A:
            return -1

        while self.A:
            self.B.append(self.A.pop())
        return self.B[-1]

    def empty(self):
        return not self.A and not self.B

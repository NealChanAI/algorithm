# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 14:25
#    @Description   : 206. 反转链表
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        反转链表
        :param head:
        :return:
        """
        if not head:
            return

        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reverseList_(self, head,):
        """
        递归写法：
        递归函数定义：
        :param head:
        :return:
        """


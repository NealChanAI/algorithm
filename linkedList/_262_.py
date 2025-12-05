# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-04 20:47
#    @Description   : 
#
# ===============================================================


"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""


class LinkedList():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        1. 非空判断
        2. pre, cur, next指针

        """
        if not head:
            return

        pre, cur = None, head

        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre

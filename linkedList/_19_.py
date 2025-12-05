# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-05 17:26
#    @Description   : 
#
# ===============================================================


"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        1. 非空判断
        2. 双指针
        """
        if not head or n < 0:
            return

        dummy = ListNode(-1)
        dummy.next = head
        p, l, r = dummy, head, head

        for _ in range(n):
            if not r.next:
                return
            r = r.next

        while r and r.next:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next

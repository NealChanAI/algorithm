# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-27 15:36
#    @Description   : #19
#
# ===============================================================


"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""

class ListNode:
    def __init__(self, val):
        self.val = val


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        double pointers
        """
        dummy = ListNode(-1)
        dummy.next = head

        l, r = dummy, dummy
        for _ in range(n):
            if not r.next:
                return
            r = r.next

        while r and r.next:
            l = l.next
            r = r.next
        l.next = l.next.next

        return dummy.next

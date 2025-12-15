# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/13 09:42
#    @Description   : 
#
# ===============================================================


"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        1. 双指针
        """
        if not l1 and not l2:
            return

        dummy = ListNode(-1)
        p, p1, p2 = dummy, l1, l2

        while p1 and p2:
            if p1.val >= p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next

            p = p.next

        if p1:
            p.next = p1

        if p2:
            p.next = p2

        return dummy.next

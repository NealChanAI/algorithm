# -*- coding: utf-8 -*-
# ===============================================================
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLists(self, list1, list2):
        """合并两个有序链表"""
        dummy = ListNode(-1)
        p = dummy
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val >= p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next

            tmp = p.next
            tmp.next = None
            p.next = tmp
            p = p.next

        if p1:
            p.next = p1

        if p2:
            p.next = p2

        return dummy.next





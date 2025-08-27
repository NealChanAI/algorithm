# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-27 16:43
#    @Description   : #160
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def get_intersection_node(self, headA, headB):
        """
        1. 非空判断
        2. 双指针
        """
        if not headA or not headB:
            return

        p1, p2 = headA, headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB

            if p2:
                p2 = p2.next
            else:
                p2 = headA

        return p1
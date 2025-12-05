# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-05 17:54
#    @Description   : 
#
# ===============================================================


"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
"""


class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        1. 非空判断
        2. 遍历完原始链表之后再接另外一条
        """

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




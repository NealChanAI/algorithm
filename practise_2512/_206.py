# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/12 20:36
#    @Description   : 
#
# ===============================================================


"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        双指针
        """
        if not head:
            return head

        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre

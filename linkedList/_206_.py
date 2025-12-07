# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/7 20:20
#    @Description   : 
#
# ===============================================================


"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""


class Solution:
    def reverse(self, head):
        """
        1. 非空判断
        2. pre, cur, next
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

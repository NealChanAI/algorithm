# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-02 11:34
#    @Description   : 
#
# ===============================================================


"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse_k_group(self, head, k):
        """递归法
        base case: 为none或者子链表长度不够K
        """

        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        p = dummy

        for _ in range(k):
            if not p.next:
                return head

        sub_head = p.next
        p.next = None
        self._reverse(head)
        head.next = self.reverse_k_group(sub_head, k)

        return p

    def _reverse(self, node):
        """反转链表"""

        if not node:
            return

        pre, cur = None, node
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre





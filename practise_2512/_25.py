# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/12 21:01
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
    def reverseKGroup(self, head, k):
        """
        递归实现
        """
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        a = dummy

        for _ in range(k):
            if not a.next:
                return head
            a = a.next

        sub_head = a.next
        a.next = None

        new_head = self.reverse(head)
        head.next = self.reverseKGroup(sub_head, k)

        return new_head

    def reverse(self, head):
        """反转链表"""
        if not head:
            return
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre





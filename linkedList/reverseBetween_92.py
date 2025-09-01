# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-01 19:28
#    @Description   : #92
#
# ===============================================================


"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse(self, head):
        """
        翻转链表
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

    def reverse_between(self, head, m, n):
        """
        迭代思路
        """
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head
        l1, l2 = dummy, dummy
        for _ in range(m-1):
            l1 = l1.next

        sub_head = l1.next

        for _ in range(n):
            l2 = l2.next
        third_p = l2.next
        l2.next = None

        l1.next = self.reverse(sub_head)
        sub_head.next = third_p

        return dummy.next




# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/14 19:33
#    @Description   : 
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
    def reverseBetween(self, head, left, right):
        """
        1. 非空判断
        2. 虚拟头节点
        3. 双指针找到left-1节点和right节点
        """
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head

        l, r = dummy, dummy

        for _ in range(left-1):
            l = l.next

        for _ in range(right):
            r = r.next

        l.next = self.reverseUntil(l.next, r.next)

        return dummy.next

    def reverseUntil(self, head, node):
        pre, cur = None, head
        while cur != node:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        head.next = node

        return pre

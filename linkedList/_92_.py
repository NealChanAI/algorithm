# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/7 20:24
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

    def reverseBetween(self, head, left, right):
        """
        1. 非空判断
        2. 虚拟头节点
        3. 先找到left和right分别的节点
        4. 反转left, right这段
        5. 拼接
        """
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head

        l, r = dummy, dummy

        for _ in range(left-1):
            if not l:
                return
            l = l.next

        for _ in range(right):
            if not r:
                return
            r = r.next

        third_head = r.next
        r.next = None
        middle_tail = l.next
        middle_head = self.reverse(middle_tail)

        l.next = middle_head
        middle_tail.next = third_head

        return dummy.next







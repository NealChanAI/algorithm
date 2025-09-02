# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-02 14:14
#    @Description   : #143
#
# ===============================================================


"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def find_middle(self, head):
        """
        找链表的中点
        """
        if not head:
            return
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

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

    def reorderList(self, head):
        """
        1. 找到链表中点, 拆分链表
        2. 反转链表
        3. 链表拼接
        """
        if not head:
            return


        middle = self.find_middle(head)
        second_part = middle.next
        middle.next = None

        new_head = self.reverse(second_part)

        # 原地修改
        while head and new_head:
            p1 = head.next
            p2 = new_head.next

            head.next = new_head
            new_head.next = p1

            head = p1
            new_head = p2



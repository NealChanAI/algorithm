# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-15 16:16
#    @Description   : 
#
# ===============================================================


"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


class Solution:
    def reorderList(self, head):
        """
        1. 找中点
        2. 反转链表
        3. 拼接链表
        """
        if not head:
            return

        middle = self.find_middle(head)
        later = middle.next
        middle.next = None
        tail = self.reverse(later)

        p1, p2 = head, tail

        while p1 and p2:
            p1_next = p1.next
            p2_next = p2.next

            p1.next = p2
            p2.next = p1_next

            p1 = p1_next
            p2 = p2_next

    def find_middle(self, head):
        """找链表的重点"""
        if not head:
            return

        # dummy = ListNode(-1)
        # dummy.next = head
        s, f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next

        return s

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

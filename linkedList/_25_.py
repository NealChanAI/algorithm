# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/7 20:43
#    @Description   : 
#
# ===============================================================


"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""


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

    def reverseKGroup(self, head, k):
        """
        递归实现：
           返回每K个节点一组进行反转的链表
           base case: 链表长度不足k或为none
        """
        if not head:
            return

        p = head
        for _ in range(k-1):
            if not p:
                return head
            p = p.next

        if not p:
            return head
        sub_head = p.next
        p.next = None

        new_head = self.reverse(head)
        head.next = self.reverseKGroup(sub_head, k)

        return new_head











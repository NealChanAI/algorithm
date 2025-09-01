# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-01 17:52
#    @Description   : #2
#
# ===============================================================


"""
给你两个 非空 的链表，表示两个非负的整数。
它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def add_two_numbers(self, l1, l2):
        """
        双指针
        使用临时变量存储
        """
        # 非空判断
        if not l1 and not l2:
            return

        dummy = ListNode(-1)
        p, p1, p2 = dummy, l1, l2
        carry = 0

        while p1 or p2:
            val_1 = p1.val if p1 else 0
            val_2 = p2.val if p2 else 0
            _sum = val_1 + val_2 + carry
            tmp = _sum % 10
            carry = _sum // 10
            p.next = ListNode(tmp)

            p1 = p1.next if p1 else p1
            p2 = p2.next if p2 else p2
            p = p.next

        if carry != 0:
            p.next = ListNode(carry)

        return dummy.next






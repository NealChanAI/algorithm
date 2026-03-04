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



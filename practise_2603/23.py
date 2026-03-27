# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 12:49
#    @Description   : 
#
# ===============================================================


"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""

import heapq


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):

        dummy = ListNode(-1)
        p = dummy

        pq = []

        for node in lists:
            if node:
                heapq.heappush(pq, (node.val, node))

        while pq:
            node_val, node = heapq.heappop(pq)
            p.next = node
            p = p.next

            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))

        return dummy.next







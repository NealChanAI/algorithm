# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-15 16:41
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
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists):
        """使用最小堆实现"""

        if not lists:
            return

        dummy = ListNode(-1)
        p = dummy

        pq = []

        for lst in lists:
            if not lst:
                continue
            heapq.heappush(pq, (lst.val, lst))

        while pq:
            min_node = heapq.heappop(pq)
            p.next = min_node
            p = p.next

            if min_node.next:
                heapq.heappush(pq, (min_node.next.val, min_node.next))

        return dummy.next

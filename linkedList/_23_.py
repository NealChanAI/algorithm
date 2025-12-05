# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-05 15:56
#    @Description   : 
#
# ===============================================================


"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""

import heapq


# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#     def __lt__(self, other):
#         return self.val < other.val


class Solution:
    def mergeKLists(self, lists):
        """
        1. 非空判断
        2. 使用heapq来存储每个链表的值, 然后每次输出最小值
        """
        if not lists:
            return

        # 构造虚拟头节点
        dummy = ListNode(-1)
        p = dummy

        ListNode.__lt__ = lambda a, b: a.val < b.val

        lst = []
        for l in lists:
            if l:
                heapq.heappush(lst, (l.val, l))

        while lst:
            val, node = heapq.heappop(lst)
            p.next = node
            if node.next:
                heapq.heappush(lst, (node.next.val, node.next))

            p = p.next

        return dummy.next




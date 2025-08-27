# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-27 14:45
#    @Description   : #23
#
# ===============================================================


import heapq


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def merge_k_lists(self, lists):
        """
        heapq最小堆获取几个list中的最小节点
        """
        if not lists:
            return

        pq = []
        for head in lists:
            if not head:
                continue
            heapq.heappush(pq, head)

        dummy = ListNode(-1)
        p = dummy

        while pq:
            node = heapq.heappop(pq)
            p.next = node

            if node.next:
                heapq.heappush(pq, node.next)

            p = p.next

        return dummy.next









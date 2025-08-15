# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 11:05
#    @Description   : 23. 合并K个升序列表
#
# ===============================================================


import heapq


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        类似于合并两个升序列表，多个指针指向多个链表，使用优先级队列来获取最小值以及对应的链表
        :param lists:
        :return:
        """
        if not lists:
            return

        pq = []
        res = []
        dummy = ListNode(-1)
        p = dummy

        ListNode.__lt__ = lambda a, b: a.val < a.val

        for lst in lists:
            if lst:
                heapq.heappush(pq, lst)

        while pq:
            node = heapq.heappop(pq)
            p.next = node
            if node.next:
                heapq.heappush(pq, node.next)
            tmp = p.next
            tmp.next = None
            p = tmp

        return dummy.next


